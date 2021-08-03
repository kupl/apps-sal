class Solution:
    def kthFactor(self, n, k):

        solution_space = list([x for x in list(range(1, n + 1)) if n % x == 0])
        if len(solution_space) < k:
            return -1
        else:
            return list([x for x in list(range(1, n + 1)) if n % x == 0])[k - 1]
