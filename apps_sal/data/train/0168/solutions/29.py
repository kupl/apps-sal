class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        cnts = collections.defaultdict(int)
        for ch in s:
            cnts[ch] += 1
        odds, evens = [], []
        for ch in cnts:
            if cnts[ch] % 2 == 1:
                odds.append(ch)
            else:
                evens.append(ch)
        return len(odds) <= k


class Solution1:
    def canConstruct(self, s: str, k: int) -> bool:
        cnts = collections.defaultdict(int)
        for ch in s:
            cnts[ch] += 1
        odds, evens = [], []
        for ch in cnts:
            if cnts[ch] % 2 == 1:
                odds.append(ch)
            else:
                evens.append(ch)
        if len(odds) > k:
            return False
        for i in range(len(odds)):
            k -= 1
            ch = odds.pop()
            cnts[ch] -= 1
            if cnts[ch] > 0:
                evens.append(ch)
        while k > len(evens):
            if not evens:
                return False
            ch = evens.pop()
            k -= 2
            cnts[ch] -= 2
            if cnts[ch] > 0:
                evens.append(ch)
        return True
