class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        left = [-1] * (n+2)
        right = [-1] * (n+2)
        
        ans = -1
        cnt = collections.Counter()
        for i, v in enumerate(arr):
            left[v] = right[v] = v
            l = r = v
            if left[v-1] != -1:
                l = left[v-1]
                cnt[v - l] -= 1
            if right[v+1] != -1:
                r = right[v+1]
                cnt[r - v] -= 1
            right[l] = r
            left[r] = l
            cnt[r - l + 1] += 1
            if cnt[m] > 0:
                ans = i + 1
        return ans
