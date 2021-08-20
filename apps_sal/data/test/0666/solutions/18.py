import math
n = int(input())
ans = (math.sqrt(1 + 8 * n) - 1) / 2
if ans % 1 == 0:
    print(int(ans))
else:
    ans = int(ans)
    ans = (ans * ans + ans) / 2
    print(int(n - ans))
