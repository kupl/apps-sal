class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        seen = {}
        for num in arr:
            remainder = num % k
            if remainder in seen:
                seen[remainder] -= 1
                if seen[remainder] == 0:
                    del seen[remainder]
            elif remainder == 0:
                seen[remainder] = 1
            else:
                seen[k - remainder] = seen.get(k - remainder, 0) + 1
        return len(seen) == 0
