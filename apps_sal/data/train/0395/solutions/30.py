class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0
        odd_dict = dict()
        even_dict = dict()
        n = len(A)
        A_inc = sorted([(A[i], i) for i in range(len(A))])
        A_dec = sorted([(-A[i], i) for i in range(len(A))])
        odd_dict[A_inc[-1][1]] = -1
        even_dict[A_dec[-1][1]] = -1
        for i in range(n - 1):
            j = i + 1
            while j <= n - 1 and A_inc[j][1] < A_inc[i][1]:
                j += 1
            if j == n:
                odd_dict[A_inc[i][1]] = -1
            else:
                odd_dict[A_inc[i][1]] = A_inc[j][1]
            j = i + 1
            while j <= n - 1 and A_dec[j][1] < A_dec[i][1]:
                j += 1
            if j == n:
                even_dict[A_dec[i][1]] = -1
            else:
                even_dict[A_dec[i][1]] = A_dec[j][1]
        print(odd_dict)
        print(even_dict)
        cnt = 1
        for i in range(n - 1):
            j = i
            odd_flag = True
            while j != n - 1 and j != -1:
                if odd_flag:
                    j = odd_dict[j]
                else:
                    j = even_dict[j]
                odd_flag = not odd_flag
            if j == n - 1:
                cnt += 1
        return cnt
