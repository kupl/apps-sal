class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        preList = [0]
        ALen = len(A)
        for i in range(1, ALen):
            if A[i] < A[preList[-1]]:
                preList.append(i)
        # print(preList)
        ans = 0
        preR = len(preList) - 1
        for i in range(ALen - 1, -1, -1):
            l = 0
            while preR > 0 and preList[preR] >= i:
                preR -= 1
            r = preR
            # r = len(preList)-1
            if A[i] < A[preList[l]] and A[i] >= A[preList[r]]:
                while r > l:
                    # print(l, r)
                    m = (r + l) // 2
                    if A[preList[m]] < A[i]:
                        r = m
                    elif A[preList[m]] > A[i]:
                        l = m + 1
                    else:
                        l = m
                        r = m - 1
                # print(i, preList[l])
                ans = max(ans, i - preList[l])
            elif A[i] >= A[preList[l]]:
                ans = max(ans, i - preList[l])

        return ans
