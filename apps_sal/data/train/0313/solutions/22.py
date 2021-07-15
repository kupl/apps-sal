class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        flowers = collections.defaultdict(list)
        for idx, day in enumerate(bloomDay):
            flowers[day].append(idx)
        root = list(range(n))
        num_flowers_left = collections.Counter()
        num_flowers_right = collections.Counter()
        num_bouquets = 0
        for day in sorted(flowers.keys()):
            for idx in flowers[day]:
                start = idx - num_flowers_left[idx - 1]
                num_bouquets -= num_flowers_left[idx - 1] // k
                end = idx + num_flowers_right[idx + 1]
                num_bouquets -= num_flowers_right[idx + 1] // k
                total_num_flowers = end - start + 1
                num_bouquets += total_num_flowers // k
                num_flowers_left[end] = total_num_flowers
                num_flowers_right[start] = total_num_flowers
                if num_bouquets >= m:
                    return day
        return -1
                    
                    

