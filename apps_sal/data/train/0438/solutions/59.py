class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        l = [0] * (n + 2)
        cnt = [0] * (n + 2)
        ans = -1
        for i, x in enumerate(a):
            left, right = l[x - 1], l[x + 1]
            l[x] = l[x - left] = l[x + right] = left + right + 1
            cnt[left] -= 1
            cnt[right] -= 1
            cnt[l[x]] += 1
            if cnt[m]:
                ans = i + 1
        return ans
