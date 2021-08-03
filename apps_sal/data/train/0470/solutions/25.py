class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        ans = 0
        for i in A:
            ans += d2[target - i]

            for j in d1:
                d2[j + i] += d1[j]

            d1[i] += 1

        return ans % int(1e9 + 7)
