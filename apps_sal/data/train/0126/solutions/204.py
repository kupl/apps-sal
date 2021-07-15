from collections import Counter, deque
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring = deque([])
        ans = Counter([])
        for ch in s:
            substring.append(ch)
            while len(substring) > minSize:
                substring.popleft()
            cnt = Counter(substring)
            if (len(cnt) <= maxLetters) and (minSize <= len(substring) <= maxSize):
                ans.update({''.join(substring): 1})
        
        return ans.most_common()[0][1] if len(ans) > 0 else 0

