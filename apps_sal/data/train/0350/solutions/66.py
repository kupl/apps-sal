class Solution:
    def subarraysWithKDistinct(self, A, K):
        cnt1, cnt2 = dict(), dict()
        res, i1, i2 = 0, 0, 0
        for v in A:
            cnt1[v] = cnt1.get(v, 0) + 1
            cnt2[v] = cnt2.get(v, 0) + 1
            while len(cnt1) > K:
                cnt1[A[i1]] -= 1
                if cnt1[A[i1]] == 0:
                    del cnt1[A[i1]]
                i1 += 1
            while len(cnt2) >= K:
                cnt2[A[i2]] -= 1
                if cnt2[A[i2]] == 0:
                    del cnt2[A[i2]]
                i2 += 1
            res += i2 - i1
        return res


class Solution:
    def subarraysWithKDistinct(self, A, K):
        cnt1, cnt2 = dict(), dict()
        res, i1, i2 = 0, 0, 0
        for v in A:
            cnt1[v] = cnt1.get(v, 0) + 1
            cnt2[v] = cnt2.get(v, 0) + 1
            while len(cnt1) > K:
                X = A[i1]
                cnt1[X] -= 1
                if cnt1[X] == 0:
                    del cnt1[X]
                i1 += 1
            while len(cnt2) > K - 1:
                X = A[i2]
                cnt2[X] -= 1
                if cnt2[X] == 0:
                    del cnt2[X]
                i2 += 1
            res += i2 - i1
        return res
