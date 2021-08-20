class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        left_states = {'': -1}
        cur_state = set()
        ans = 0
        for (i, char) in enumerate(s):
            if char in 'aeiou':
                if char in cur_state:
                    cur_state.remove(char)
                else:
                    cur_state.add(char)
            cur_state_str = ''.join(sorted(list(cur_state)))
            if cur_state_str in left_states:
                ans = max(ans, i - left_states[cur_state_str])
            else:
                left_states[cur_state_str] = i
        return ans
