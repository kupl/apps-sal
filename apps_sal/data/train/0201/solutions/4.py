class Solution:

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        '\n         The most straightforward solution would be to try all possible permutations that specify the order of input in constructing a BST and counting the different ways in which the BST results. But that would take O(n!) time and O(n) space.\n         Maybe it would help to use the fact that a BST is defined recursively.\n         Does the topology of a subtree affects whether the parent subtree is valid or not?\n         No.\n         And is it possible that we get any duplicate trees when we first designate our root and then permute its subtrees? \n         No.\n         So for each node i, set i as a root and then construct/permute the left and the right subtrees. \n         The parameter we need to take care of is the list of available nodes in that subtree.\n         Memoize the results, too.\n         '

        def memoize(func):
            func.cache = cache = dict()

            def memoizer(*args):
                key = str(args)
                if key not in cache:
                    cache[key] = func(*args)
                return cache[key]
            return memoizer

        @memoize
        def count(root, lower_bound, upper_bound):
            if upper_bound < lower_bound:
                return 0
            if lower_bound == upper_bound:
                return 1
            left_combinations = max(1, sum((count(left, lower_bound, root - 1) for left in range(lower_bound, root))))
            right_combinations = max(1, sum((count(right, root + 1, upper_bound) for right in range(root + 1, upper_bound + 1))))
            return left_combinations * right_combinations
        return sum((count(root, 1, n) for root in range(1, n + 1)))
