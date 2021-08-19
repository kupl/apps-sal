class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        factorSet = set(A)
        A.sort()
        treeCount = collections.defaultdict(lambda: 1)
        n = len(A)
        end = 0
        for num in A:
            sqrt = int(math.sqrt(num) + 1)
            while end < n and A[end] <= sqrt:
                end += 1
            count = 0
            for (_, p) in zip(list(range(end)), A):
                if num % p == 0 and (q := (num // p)) in factorSet and (p <= q):
                    count += 2 * treeCount[p] * treeCount[q] if p != q else treeCount[p] * treeCount[q]
            treeCount[num] += count
        return sum(treeCount.values()) % (1000000000 + 7)
