class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def highestBit(x):
            i = 0
            while x:
                i += 1
                x = x >> 1
            return i

        def numberOfBits(x):
            i = 0
            while x:
                i += 1
                x = x & (x - 1)
            return i
        doublings = max(map(highestBit, nums))
        print(doublings)
        adds = sum(map(numberOfBits, nums))
        print(adds)
        return doublings - 1 + adds
