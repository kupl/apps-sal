import math
import numpy as np
N = int(input())

ans = []


def calc(a, ans):
    if a <= 26:
        ans.append(a % 27)
        ans.reverse()
        return ans
    elif a % 26 != 0:
        ans.append(a % 26)
        return calc(a // 26, ans)
    else:
        ans.append(26)
        return calc(a // 26 - 1, ans)


ans = calc(N, ans)
for i in range(len(ans)):
    ans[i] = chr(ans[i] + 96)

print((''.join(ans)))

