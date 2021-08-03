class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums)
        n_left = len(nums)
        count_keys = [c for c in counts if counts[c] > 0]
        count_keys.sort()

        if n_left % k != 0:
            return False

        while n_left > 0:
            while counts[count_keys[0]] == 0:
                count_keys.pop(0)
            start = count_keys[0]
            for i in range(k):
                if counts[start + i] == 0:
                    return False
                counts[start + i] -= 1
                n_left -= 1

        return True
