class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        factorSet = set(A)
        A.sort()
        treeCount = {}

        for num in A:
            count = 1
            for p, pCount in list(treeCount.items()):
                q, rem = divmod(num, p)
                if rem == 0:
                    count += pCount * treeCount.get(q, 0) 
            treeCount[num] = count
        return sum(treeCount.values()) % (1000_000_000 + 7)

