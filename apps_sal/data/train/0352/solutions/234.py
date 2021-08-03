class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        mark = {}
        queue = []
        for index, word in enumerate(words):
            mark[word] = collections.Counter(word)
            queue.append([[word], index, len(word)])
        ans = 0
        while queue:
            s, index, l = queue.pop(0)
            flag = True
            for i in range(index + 1, len(words)):
                if len(words[i]) > l + 1:
                    break
                if len(words[i]) == l + 1:
                    add = True
                    sum1 = 0
                    sum2 = 0
                    for key in list(mark[s[-1]].keys()):
                        if key not in mark[words[i]]:
                            add = False
                            break
                        sum1 += mark[s[-1]][key]
                        sum2 += mark[words[i]][key]
                    if add and (sum1 == sum2 or sum2 - sum1 == 1):
                        queue.append([s + [words[i]], i, l + 1])
                        flag = False
            if flag:
                ans = max(ans, len(s))
        return ans
