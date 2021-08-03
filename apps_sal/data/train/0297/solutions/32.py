class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        s = set()

        def tot(curr, rem):
            nonlocal s
            if curr[-1]:
                s.add(tuple(curr[-1]))
            for i in range(len(rem)):
                el = curr[-1]
                if rem[i] == el:
                    continue
                tot(curr + [el + [rem[i]]], rem[:i] + rem[i + 1:])
        tot([[]], tiles)
        return len(s)
