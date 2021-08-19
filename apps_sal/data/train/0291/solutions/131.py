class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        A = [i % 2 for i in arr]
        n = len(A)

        lst = [[0, 0]]
        lst[0][A[0] & 1] = 1

        for i in range(1, n):
            if A[i]:
                lst.append([lst[-1][1], 1 + lst[-1][0]])
            else:
                lst.append([1 + lst[-1][0], lst[-1][1]])

        # print(lst)

        return sum([x[1] for x in lst]) % (10**9 + 7)
