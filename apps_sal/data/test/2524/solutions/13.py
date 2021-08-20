import numpy as np
import sys
input = sys.stdin.readline
'\na=[]\nb=[]\nfor i in range():\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'
n = int(input())
a = np.array([int(i) for i in input().split()])
ans = 0
for i in range(60):
    cnt = np.count_nonzero(a & 1)
    ans += (n - cnt) * cnt * 2 ** i
    if ans >= 10 ** 9 + 7:
        ans %= 10 ** 9 + 7
    a >>= 1
print(ans)
