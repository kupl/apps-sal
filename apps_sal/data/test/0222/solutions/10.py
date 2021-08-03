import sys
import math
from functools import lru_cache


@lru_cache(maxsize=None)
def solution(nstr, nint, acc):
    msf = float('inf')
    if (math.sqrt(nint) - int(math.sqrt(nint))) == 0.0:
        return acc
    for i in range(len(nstr)):
        mstr = nstr[:i] + nstr[i + 1:]
        if mstr:
            if mstr[0] == '0':
                continue
            msf = min(msf, solution(mstr, int(mstr), acc + 1))
    if msf == float('inf'):
        return float('inf')
    return msf


n = sys.stdin.readline().strip()

res = solution(n, int(n), 0)
if res == float('inf'):
    print(-1)
else:
    print(res)
