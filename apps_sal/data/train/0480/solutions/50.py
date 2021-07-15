class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        states = [{0: 1}, {}]
        base = 0
        mod = 1000000007
        shift = [1, 0, -1]
        for k in range(0, steps):
            nxt = (base+1)%2
            states[nxt].clear()
            for p in states[base].keys():
                for j in range(0, 3):
                    np = p+shift[j]
                    if 0 <= np < arrLen:
                        if np not in states[nxt].keys():
                            states[nxt][np] = 0
                        states[nxt][np] = (states[nxt][np] + states[base][p]) % mod
            base = nxt
        return states[base][0]
