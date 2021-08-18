from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return 0


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        def get_length(x, y):
            s = 0
            while x + y in A:
                s += 1
                x, y = y, x + y
            return s
        if len(A) < 3:
            return 0
        ans = 0
        sum_lim = A[-1]
        for fi in range(len(A) - 2):
            curr_ans = 0
            temp_fi = fi
            si = temp_fi + 1
            while si < len(A):
                reqd_sum = A[temp_fi] + A[si]
                if reqd_sum > sum_lim:
                    break
                pres = BinarySearch(A, reqd_sum)
                if pres:
                    curr_ans = 1 + get_length(A[si], A[pres])
                    ans = max(ans, curr_ans)
                si += 1
        return ans + 2 if ans > 0 else ans
