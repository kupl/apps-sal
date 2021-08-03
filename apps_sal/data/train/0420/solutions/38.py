from collections import Counter


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        _max = 0
        vowels = 'aeiou'

        def counter_to_tuple(counter):
            res = []
            for v in vowels:
                res.append(counter[v] % 2)
            return tuple(res)

        ss_counter = Counter()
        cache = {(0, 0, 0, 0, 0): -1}
        length = 0
        for ind, ss in enumerate(s):
            if ss in vowels:
                ss_counter[ss] += 1
            counter_tuple = counter_to_tuple(ss_counter)
            if counter_tuple in cache:
                length = max(length, ind - cache[counter_tuple])
            else:
                cache[counter_tuple] = ind
        return length
