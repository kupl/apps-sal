
def is_pre(s1, s2):
    c = 0
    i = 0
    for j in range(len(s2)):
        if i == len(s1) or s1[i] != s2[j]:
            c += 1
        else:
            i += 1
    return c == 1


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        m = {}
        incount = {}
        q = collections.deque()
        seen = set()
        for i in range(n):
            if i not in incount:
                q.append(i)
            wn = len(words[i])
            for j in range(i + 1, n):
                jn = len(words[j])
                if jn > wn + 1:
                    break
                if jn == wn + 1 and is_pre(words[i], words[j]):
                    m.setdefault(i, []).append(j)
                    incount[j] = incount.get(j, 0) + 1
        lev = 0
        while q:
            lev += 1
            for i in range(len(q)):
                u = q.popleft()
                for v in m.get(u, []):
                    if v not in seen:
                        q.append(v)
                        seen.add(v)
        return lev
