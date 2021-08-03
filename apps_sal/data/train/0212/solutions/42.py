class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        num_trees = {}
        A.sort()
        A_set = set(A)
        for i in range(len(A)):
            curr_num = A[i]
            num_trees[curr_num] = 1
            for j in range(i):
                if (A[i] % A[j] == 0):
                    if (A[i] // A[j]) in A_set:
                        num_trees[curr_num] += (num_trees[A[j]] * num_trees[A[i] // A[j]])
        total = 0
        for key in num_trees:
            total += num_trees[key]
            total %= (10**9 + 7)
        return total
