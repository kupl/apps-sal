class Solution:
    def numWays(self, s: str) -> int:
        from math import factorial
        c = s.count('1')
        if c % 3 != 0:
            return 0
        if c == 0:
            pos = len(s) - 1
            numerator = factorial(pos)
            denominator = factorial(2) * factorial(pos - 2)
            return int((numerator / denominator) % (10**9 + 7))

        num1_each_group = int(c / 3)

        track = 0
        track_g1_l1 = 0
        track_g2_f1 = 0
        for i in range(len(s)):
            if s[i] == '1':
                track += 1
            if track == num1_each_group:
                track_g1_l1 = i
                break
        track = 0
        for i in range(len(s)):
            if s[i] == '1':
                track += 1

            if track == num1_each_group + 1:
                track_g2_f1 = i
                break
        gap1 = track_g2_f1 - track_g1_l1

        track = 0
        track_g2_l1 = 0
        for i in range(len(s)):
            if s[i] == '1':
                track += 1
            if track == num1_each_group * 2:
                track_g2_l1 = i
                break

        track = 0
        track_g3_f1 = 0
        for i in range(len(s)):
            if s[i] == '1':
                track += 1
            if track == num1_each_group * 2 + 1:
                track_g3_f1 = i
                break

        gap2 = track_g3_f1 - track_g2_l1
        return int(gap1 * gap2 % (10**9 + 7))
