class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        count = collections.Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
        '''
        If a string have occurrences x times,
any of its substring must appear at least x times.

There must be a substring of length minSize, that has the most occurrences.
So that we just need to count the occurrences of all substring with length minSize.'''
