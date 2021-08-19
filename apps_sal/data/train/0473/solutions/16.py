class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        (A, pre) = ([arr[0]], arr[0])
        for ii in arr[1:]:
            pre ^= ii
            A.append(pre)
        res = 0
        for ii in range(N):
            for kk in range(ii + 1, N):
                (a_i, a_k) = (A[ii - 1] if ii else 0, A[kk])
                a_ik = a_k ^ a_i
                if not a_ik:
                    res += kk - ii
        return res
