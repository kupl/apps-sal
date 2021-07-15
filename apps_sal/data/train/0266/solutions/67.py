class Solution:
    def numSplits(self, s: str) -> int:
        left_map = {}
        right_map = {}
        unique_right = 0
        unique_left = 0
        for i in range(len(s)):
            if s[i] not in right_map:
                right_map[s[i]] = 1
                unique_right += 1
            else:
                right_map[s[i]] += 1
        good_split = 0
        for i in range(len(s)):
            # add to left map
            if s[i] not in left_map:
                left_map[s[i]] = 1
                unique_left += 1
            else:
                left_map[s[i]] += 1

            # remove from right map
            if right_map[s[i]] == 1:
                unique_right -= 1
            right_map[s[i]] -= 1
            if unique_left == unique_right:
                good_split += 1
        return good_split
