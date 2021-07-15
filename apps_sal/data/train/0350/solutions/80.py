class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        keyCounter = defaultdict(int)
        ALen = len(A)
        l = 0
        r = 0
        ans = 0
        KNow = 0
        while r <= ALen:
            if KNow == K:
                ans += 1
                temp = 0
                while r+temp < ALen and keyCounter[A[r+temp]] > 0:
                    ans += 1
                    temp += 1
                if keyCounter[A[l]] > 0:
                    keyCounter[A[l]] -= 1
                if keyCounter[A[l]] == 0:
                    KNow -= 1
                l += 1
            elif KNow < K:     
                if r == ALen:
                    return ans
                if keyCounter[A[r]] == 0:
                    KNow += 1
                keyCounter[A[r]] += 1
                r += 1
            else:
                if keyCounter[A[l]] > 0:
                    keyCounter[A[l]] -= 1
                if keyCounter[A[l]] == 0:
                    KNow -= 1
                l += 1
        return ans
