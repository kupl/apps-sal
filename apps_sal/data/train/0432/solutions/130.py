class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        for n in sorted(count):
            if count[n] == 0:
                continue
            occ = count[n]
            count[n] = 0
            for i in range(n + 1, n + k):
                count[i] -= occ
                if count[i] < 0:
                    return False
        return True
