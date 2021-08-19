class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # Convert array to 0 and 1s
        bits = [1 if x > 8 else -1 for x in hours]
        # Problem becomes: find the longest interval bits[i:j] where sum(bits[i:j]) > 0
        # Get prefix sum of bits
        pref = [0] * (len(bits) + 1)
        for i in range(1, len(bits) + 1):
            pref[i] = pref[i - 1] + bits[i - 1]
        # Problem becomes: find the longest interval pref[i:j] where pref[j] > pref[i]
        # Sort index of pref by value. Problem becomes: find the largest sorted_pref[j]-sorted_pref[i] where j > i
        # Greedy to solve the new problem
        ans = 0
        min_val = len(bits) + 1
        for y in sorted(enumerate(pref), key=lambda x: (x[1], -x[0])):
            min_val = min(min_val, y[0])
            ans = max(ans, y[0] - min_val)
        return ans
