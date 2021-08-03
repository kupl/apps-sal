class Solution:
    def numWays(self, s: str) -> int:
        L = len(s)
        count = collections.Counter(s)
        if count['0'] == L:
            return (L - 1) * (L - 2) // 2
        if count['1'] % 3:
            return 0
        K = count['1'] // 3
        prefix = [0] * L
        for k, v in enumerate(s):
            prefix[k] = (v == '1') + (prefix[k - 1] if k else 0)
        count1 = collections.Counter(prefix)
        return count1[K] * count1[K * 2] if count1[K * 3] > 0 else 0

    def numWays(self, s: str) -> int:
        L, M = len(s), 10 ** 9 + 7
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
