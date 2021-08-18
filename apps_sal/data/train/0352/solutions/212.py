class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        l = [1 for i in range(len(words))]
        words.sort(key=lambda x: len(x))
        res = [[i] for i in words]
        for i in range(1, len(words)):
            for j in range(i):
                if len(words[j]) + 1 == len(words[i]):
                    x = {}
                    for a in words[j]:
                        if a in x:
                            x[a] += 1
                        else:
                            x[a] = 1
                    ctr = 0
                    for a in words[i]:
                        if a not in x:
                            ctr += 1
                        elif x[a] == 0:
                            ctr += 1
                        else:
                            x[a] -= 1
                    if ctr == 1 and l[i] < (l[j] + 1):
                        res[i] = [i for i in res[j]]
                        res[i].append([words[i]])
                        l[i] = l[j] + 1
        return max(l)
