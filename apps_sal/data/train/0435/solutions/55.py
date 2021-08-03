class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        prefixMod = 0
        hashTable = collections.defaultdict(int)
        total = 0
        curSum = 0
        hashTable[0] = 1

        for i, x in enumerate(A):

            prefixMod = prefixMod + x

            prefixMod = prefixMod % K

            total += hashTable[prefixMod]

            hashTable[prefixMod] += 1

        return total
