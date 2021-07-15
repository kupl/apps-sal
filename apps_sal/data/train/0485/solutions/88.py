class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        ALen = len(A)
        flips = []
        prevF = 0
        ans = 0
        l = 0
        for i, num in enumerate(A):
            temp = 0
            while l+temp < len(flips) and flips[l+temp] + K- 1 < i:
                temp += 1
            l += temp
            prevF = prevF - temp
            if (prevF%2 and num == 0) or (prevF%2 == 0 and num == 1):
                continue
            else:
                ans += 1
                prevF += 1
                flips.append(i)
            #         if num == 0:
            #         continue
            #     else:
            #         ans += 1
            #         prevF += 1
            #         flips.append(i)
            # else:
            #     if num == 0:
            #         ans += 1
            #         prevF += 1
            #         flips.append(i)
            #     else:
            #         continue
        if flips != [] and flips[-1] + K -1 >= ALen:
            return -1
        return ans
