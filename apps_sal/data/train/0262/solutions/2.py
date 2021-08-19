class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        words.append(result)
        (M, N) = (len(words), max(list(map(len, words))))
        dic = {}
        rem = [None] * 10
        lead = set([w[0] for w in words])

        def backtrack(i, j, cur):
            if j == N:
                return cur == 0
            if i == M:
                return not cur % 10 and backtrack(0, j + 1, cur // 10)
            if j >= len(words[i]):
                return backtrack(i + 1, j, cur)
            t = words[i][~j]
            sign = 1 if i < M - 1 else -1
            if t in dic:
                return backtrack(i + 1, j, cur + dic[t] * sign)
            else:
                for (k, r) in enumerate(rem):
                    if not r and (k or t not in lead):
                        dic[t] = k
                        rem[k] = t
                        if backtrack(i + 1, j, cur + dic[t] * sign):
                            return True
                        del dic[t]
                        rem[k] = None
            return False
        return backtrack(0, 0, 0)
