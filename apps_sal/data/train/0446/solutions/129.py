class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_count = defaultdict(int)
        for i in arr:
            num_count[i] += 1
        h = []
        key_count = 0
        for key in list(num_count.keys()):
            heapq.heappush(h, (num_count[key], key))
            key_count += 1
        result = key_count
        while k > 0:
            (count, num) = heapq.heappop(h)
            k = k - count
            if k >= 0:
                result -= 1
                continue
            if k < 0:
                break
        return result
