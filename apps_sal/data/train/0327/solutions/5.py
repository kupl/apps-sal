class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        seen_set = set()
        longest_substring = ''
        while end < len(s):
            end += 1
            currentelem = s[end - 1]
            if currentelem not in seen_set:
                seen_set.add(currentelem)
                if end - start > len(longest_substring):
                    longest_substring = s[start:end]
            else:
                while start < end - 1:
                    if s[start] != currentelem:
                        seen_set.remove(s[start])
                        start += 1
                    else:
                        start += 1
                        break
        return len(longest_substring)
