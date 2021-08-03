class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        ret = 0
        root_value_to_tree_number = collections.defaultdict(int)

        for i in range(len(A)):
            occurrences = 1

            for j in range(i - 1, -1, -1):
                if (A[i] % A[j] == 0):
                    required_root_value = A[i] // A[j]
                    occurrences += root_value_to_tree_number[required_root_value] * root_value_to_tree_number[A[j]]

            root_value_to_tree_number[A[i]] = occurrences
            ret += occurrences

        return ret % 1000000007
