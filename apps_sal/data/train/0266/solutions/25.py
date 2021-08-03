# time complexity: O(26N), N = len(s)
# class Solution:
#    def numSplits(self, s: str) -> int:
#        N = len(s)
#        freq = [[0] * (N+1) for _ in range(26)] # cumulative freq of each character
#        for i in range(1, N+1):
#            for j in range(26):
#                if ord(s[i-1]) - ord('a') == j:
#                    freq[j][i] = freq[j][i-1] + 1
#                else:
#                    freq[j][i] = freq[j][i-1]
#
#        good = 0
#        for i in range(1, N):
#            left = 0
#            right = 0
#            for j in range(26):
#                if freq[j][i] > 0: # there is at least one chr(ord(j) + ord('a')) on the left of s[i]
#                    left += 1
#                if freq[j][i] < freq[j][-1]: # there is at least one chr(ord(j) + ord('a')) on the right of s[i]
#                    right += 1
#            if left == right:
#                good += 1
#        return good

# time complexity: O(3N), N = len(s)
class Solution:
    def numSplits(self, s: str) -> int:
        N = len(s)

        left = [0] * (N + 1)  # unique char in s[:left], exclude left
        seen = set()
        for i in range(1, N + 1):
            c = s[i - 1]
            if c not in seen:
                left[i] = left[i - 1] + 1
                seen.add(c)
            else:
                left[i] = left[i - 1]

        right = [0] * (N + 1)  # unique char in s[right:], include right
        seen.clear()
        for i in range(N - 1, -1, -1):
            c = s[i]
            if c not in seen:
                right[i] = right[i + 1] + 1
                seen.add(c)
            else:
                right[i] = right[i + 1]

        good = 0
        for i in range(N + 1):
            if left[i] == right[i]:
                good += 1
        return good
