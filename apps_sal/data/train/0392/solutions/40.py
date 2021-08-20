class Solution:

    def numWays(self, s: str) -> int:
        ones_count = s.count('1')
        n = len(s)
        if ones_count == 0:
            return (n - 2) * (n - 1) // 2 % (10 ** 9 + 7)
        if ones_count % 3 != 0:
            return 0
        no_of_ones = ones_count / 3
        (count, count_1st, count_2nd) = (0, 0, 0)
        for i in s:
            if i == '1':
                count += 1
            if count == no_of_ones:
                count_1st += 1
            if count == 2 * no_of_ones:
                count_2nd += 1
        return count_1st * count_2nd % (10 ** 9 + 7)
