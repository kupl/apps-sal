class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        cnt = 0
        choice = ['a','b','c']
        ret = []
        def backTrack(lastCh, idx, l):
            nonlocal cnt, ret
            if idx == n:
                cnt += 1
                if cnt == k:
                    ret = l
                    return True
                return False
            for ch in choice:
                if ch == lastCh:
                    continue
                l.append(ch)
                if backTrack(ch, idx+1, l):
                    return True
                l.pop()               
        backTrack('x', 0, [])
        return ''.join(ret)

