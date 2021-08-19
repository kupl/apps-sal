import sys
input = sys.stdin.readline
'\na=[]\nb=[]\nfor i in range():\n    A, B = map(int, input().split())\n    a.append(A)   \n    b.append(B)'
n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * (n // i) * (1 + n // i) // 2
print(ans)
