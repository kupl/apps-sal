import math


class Solution1:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        N = len(A)
        if N <= 1:
            return False
        max_sum = sum(A)
        sums = [0] * (max_sum + 1)
        for i in range(N):
            num = A[i]
            for s in range(max_sum, num - 1, -1):
                if sums[s - num]:
                    sums[s] |= sums[s - num] << 1
            sums[num] |= 1
        for l in range(1, N):
            if max_sum * l % N == 0:
                s = int(max_sum * l / N)
                if sums[s] >> l - 1 & 1:
                    return True
        return False


class Solution2:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort(reverse=True)
        N = len(A)
        if N <= 1:
            return False
        max_size = math.ceil(N / 2)
        max_sum = sum(A)
        target_mean = max_sum / N
        ans = False

        def choose(max_n, curr_n, curr_sum, next_id):
            nonlocal target_mean
            nonlocal ans
            nonlocal N
            if ans:
                return
            if curr_n > max_n:
                return
            if curr_n:
                curr_mean = curr_sum / curr_n
                if curr_mean < target_mean:
                    return
                if curr_mean == target_mean:
                    ans = True
                    return
            if next_id == N - 1:
                return
            for i in range(next_id, N):
                choose(max_n, curr_n + 1, curr_sum + A[i], i + 1)
        choose(max_size, 0, 0, 0)
        return ans


class Solution(object):

    def splitArraySameAverage(self, A):
        from fractions import Fraction
        N = len(A)
        S = sum(A)
        A = [z - Fraction(S, N) for z in A]
        if N == 1:
            return False
        left = {A[0]}
        for i in range(1, N // 2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left:
            return True
        right = {A[-1]}
        for i in range(N // 2, N - 1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right:
            return True
        sleft = sum((A[i] for i in range(N // 2)))
        sright = sum((A[i] for i in range(N // 2, N)))
        return any((-ha in right and (ha, -ha) != (sleft, sright) for ha in left))
