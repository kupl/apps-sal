class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        """
        Compute the frequency of each characters.
        Count the 奇数次的字母, 
        each palindrome can consume at most one char with odd                 frequency. thus k must >= |odd|.
        ans = k <= len(s) and k >= odd
        """
        if k > len(s):
            return False
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1
        odd = 0
        for c in freq:
            odd += freq[c] & 1
        return odd <= k
