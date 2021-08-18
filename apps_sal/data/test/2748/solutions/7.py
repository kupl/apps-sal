import heapq


class Solution:
    def letterCombinations(self, digits):
        digit_map = {'1': [""],
                     '2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z'],
                     '0': [""]}
        combs = []
        letter_q = [(0, "")]
        if not digits:
            return []
        while letter_q:
            cur = heapq.heappop(letter_q)
            cur_idx = cur[0]
            cur_str = cur[1]
            next_dig = digits[cur_idx]
            for value in digit_map[next_dig]:
                new_digit_str = (cur_idx + 1, cur_str + value)
                if cur_idx + 1 >= len(digits):
                    combs.append(new_digit_str)
                else:
                    heapq.heappush(letter_q, new_digit_str)
        return list(map(lambda x: x[1], combs))
