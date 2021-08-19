class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Stores count of remainders
        c = collections.Counter([i % k for i in arr])

        for j in c:
            # If there is a reminder of 0 check that the number of times 0 occurs is even
            # THis guarantees pairing for the rest of remainders > 0
            if j == 0:
                if c[j] % 2 != 0:
                    return False
            # If remainder is not 0
            # Check if the counts are even or have a pairing for remainders > 0
            else:
                if c[j] != c[k - j]:
                    return False
        return True
