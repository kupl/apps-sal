class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        le = len(arr)
        o = 0
        s = 0
        for i in arr:
            s += i
            if s % 2:
                o += 1
        return (o * ((le - o) + 1)) % 1000000007
