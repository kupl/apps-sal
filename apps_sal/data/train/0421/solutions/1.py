class Solution:       
    def lastSubstring(self, s: str) -> str:
        curr_value = 0
        max_value = 0
        max_idx = 0
        char_to_id = {c: i for i, c in enumerate(sorted(set(s)))}
        radix = len(char_to_id) ** (len(s) - 1)
        
        for i in range(len(s) - 1, -1, -1):
            curr_value = char_to_id[s[i]] + curr_value / len(char_to_id)
            # print(curr_value)

            if curr_value > max_value:
                max_value = curr_value
                max_idx = i

        return s[max_idx:]
        # index = {c: i for i, c in enumerate(sorted(set(s)))}
        # radix, val, cur, lo = len(index), 0, 0, 0
        # for i in range(len(s) - 1, -1, -1):
        #     cur = index[s[i]] + cur / radix
        #     print(cur)
        #     if cur >= val:
        #         lo, val = i, cur
        # return s[lo:]

