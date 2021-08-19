class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = Counter([x % k for x in arr])
        for num in arr:
            if freq[num % k] == 0:
                continue
            freq[num % k] -= 1
            if freq[(k - num % k) % k] == 0:
                return False
            freq[(k - num % k) % k] -= 1
        return True
