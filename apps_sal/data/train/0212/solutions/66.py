class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        seen,A={},set(A)
        def find_all(root):
            if root in seen:
                return seen[root]
            combs=1
            for left in A:
                if root==left or root%left: continue
                right=root//left
                if right not in A: continue
                combs+=find_all(left)*find_all(right)
            seen[root]=combs
            return combs
        return sum(find_all(num) for num in A)%1000000007
