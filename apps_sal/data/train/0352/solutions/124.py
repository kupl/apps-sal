

from collections import deque


def getKey(item):
    return len(item)


def isPred(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    q1 = deque(word1)
    q2 = deque(word2)
    while q1 and q2:
        if q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        else:
            q2.popleft()
    if (not q1) and len(q2) <= 1:
        return True
    return False


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=getKey)
        dp = [1] * len(words)

        for i in range(1, len(dp)):
            for j in reversed(list(range(0, i))):
                if len(words[j]) == len(words[i]):
                    continue
                elif len(words[j]) + 1 == len(words[i]):
                    if isPred(words[j], words[i]):
                        dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break

        return max(dp)
