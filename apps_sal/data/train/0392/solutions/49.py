class Solution:

    def numWays(self, s: str) -> int:
        count_map = collections.Counter(s)
        if count_map['1'] % 3 != 0:
            return 0
        elif count_map['1'] == 0:
            if count_map['0'] < 3:
                return 0
            if count_map['0'] == 3:
                return 1
            i = 4
            res = 1
            while i <= count_map['0']:
                res += i - 2
                i += 1
            return res % 1000000007
        else:
            i = 0
            one_count = 0
            (s1_start, s1_end, s2_start, s2_end) = (-1, -1, -1, -1)
            factor = count_map['1'] // 3
            while i < len(s):
                if s[i] == '1':
                    one_count += 1
                    if one_count == factor:
                        s1_start = i
                    elif one_count == factor + 1:
                        s1_end = i
                    if one_count == factor * 2:
                        s2_start = i
                    elif one_count == factor * 2 + 1:
                        s2_end = i
                        break
                i += 1
            return (s1_end - s1_start) * (s2_end - s2_start) % 1000000007
