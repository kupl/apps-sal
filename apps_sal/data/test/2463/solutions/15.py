import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

res = [0] * n
a = sorted(a, reverse=True)
ai = 0

for i in range(0, n, 2):
    res[i] = a[ai]
    ai += 1
for i in range(1, n, 2):
    res[i] = a[ai]
    ai += 1
print((n - 1) // 2)
print(*res)
