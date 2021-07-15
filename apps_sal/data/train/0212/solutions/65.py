class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        factorSet = set(A)
        A.sort()
        treeCount = {}

        for num in A:
            count = 1
            for p, pCount in list(treeCount.items()):
                q, rem = divmod(num, p)
                if p > q:
                    break
                if rem == 0 and q in treeCount:
                    count += pCount*treeCount[q] if p == q else 2*pCount*treeCount[q]
            treeCount[num] = count
        return sum(treeCount.values()) % (1000_000_000 + 7)

