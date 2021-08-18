import sys


def input(): return sys.stdin.readline().strip("\r\n")


n, k = list(map(int, input().split()))
x = list(map(int, input().split()))
first = [k] * (n + 1)
last = [-1] * (n + 1)

for i in range(1, k + 1):
    last[x[i - 1]] = i
for i in range(k, 0, -1):
    first[x[i - 1]] = i

ans = 0
for i in range(1, n + 1):
    if last[i] == -1:
        ans += 1

for i in range(1, n):
    if first[i] >= last[i + 1]:
        ans += 1
    if first[i + 1] >= last[i]:
        ans += 1
print(ans)
