class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        #         minSize <= size <= maxSize
        #         uniqu <= maxLetters

        #         loop from 3 to 4
        #         aab abcaab

        #         aaba
        #         to find number of uniques, find the len of the set

        #         TIME: O(SN^2)
        #         SPACE: O(N)
        #         abcde length = 5
        #               size = 3

        #         abcde

        ans = 0
        counter = collections.Counter()

        for size in range(minSize, maxSize + 1):
            for j in range(len(s) - size + 1):
                substring = s[j:j + size]
                if len(set(substring)) <= maxLetters:
                    counter[substring] += 1
                    ans = max(ans, counter[substring])
#                     count = 1
#                     for k in range(j+1, len(s)-size+1):
#                         if substring == s[k:k+size]: count += 1
#                     ans = max(ans,count)
        return ans
