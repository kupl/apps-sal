class Solution:

    def numWays(self, s: str) -> int:
        (L, M) = (len(s), 10 ** 9 + 7)
        ones = s.count('1')
        if ones == 0:
            return (L - 1) * (L - 2) // 2 % M
        if ones % 3:
            return 0
        K = ones // 3
        cnt = one_count = two_count = 0
        for c in s:
            if c == '1':
                cnt += 1
            if cnt == K:
                one_count += 1
            elif cnt == K * 2:
                two_count += 1
        return one_count * two_count % M
