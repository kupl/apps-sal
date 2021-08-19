class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cur_soln = {s[:minSize]: 1}
        for end in range(minSize, len(s)):
            for start in range(end - minSize + 1, max(-1, end - maxSize), -1):
                subs = s[start:end + 1]
                cur_soln[subs] = cur_soln.get(subs, 0) + 1
        cur_best = 0
        for (s, cnt) in list(cur_soln.items()):
            if cnt > cur_best and len(set(s)) <= maxLetters:
                cur_best = cnt
        return cur_best
