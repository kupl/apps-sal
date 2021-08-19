class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        # i think u have to do smaller numbers first because the smaller set is contained within the larger set
        # returns indices

        # Greedy does not work; need to do this in n^2 time i think
        #         def solve(size, a):
        #             i= 0
        #             j = i + size
        #             m = [i,j] #max indices
        #             s = sum(a[i:j]) # current sum
        #             max_sum = s # max sum
        #             while(j != len(a)):
        #                 i+=1
        #                 j+=1
        #                 s -= a[i-1]
        #                 s += a[j-1]
        #                 if s > max_sum:
        #                     max_sum = s
        #                     m[0] = i
        #                     m[1] = j
        #             return m, max_sum

        #         m, ms = solve(min(L,M), A)
        #         # print(m, ms)
        #         # A = A[:m[0]] + A[m[1]:]
        #         # print(A)
        #         m2, ms2 = solve(max(L,M), A[:m[0]] + A[m[1]:])
        #         print(m, ms, m2, ms2)

        #         m3, ms3 = solve(max(L,M), A)
        #         m4, ms4 = solve(min(L,M), A[:m3[0]] + A[m3[1]:])
        #         print(m3, ms3, m4, ms4)
        #         return max(ms + ms2, ms3 + ms4)

        # On^2 time too slow
        # def solve(size1, size2, a):
        #     # current max
        #     curr = sum(a[0:0+size1]) + sum(a[size1: size1+size2])
        #     for i in range(len(a)-size2-size1+1):
        #         for j in range(i+size1, len(a)):
        #             temp = sum(a[i:i+size1]) + sum(a[j: j+size2]) # make this faster
        #             # temp = curr - a[j-1] + a[j+size2]
        #             # print(temp, i, i + size1, j, j + size2)
        #             if temp> curr:
        #                 curr = temp
        #     return curr
        # m = solve(L, M, A)
        # m2 = solve(M, L, A)
        # return max(m, m2)
        A = [0] + A
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        # print(A[1]-A[0])
        # print(len(A))

        def solve(l, m, a):
            curr = 0
            # for i in range(len(a)-l-m+1):
            for i in range(len(a) - l + 1):
                for j in range(i + l, len(a) - m):
                    # print(i, i+l, j, j+m, a[i+l] - a[i], a[j+m] - a[j])
                    temp = a[i + l] - a[i] + a[j + m] - a[j]
                    if temp > curr:
                        curr = temp
            return curr

        m2 = solve(M, L, A)
        m = solve(L, M, A)
        # return m2
        # print(m, m2)
        return max(m, m2)
