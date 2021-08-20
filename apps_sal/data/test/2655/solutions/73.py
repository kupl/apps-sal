from math import floor
import sys
input = sys.stdin.readline
'\na=[]\nb=[]\nfor i in range():\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(1, n):
    ans += a[n - 1 - floor(i / 2)]
print(ans)
