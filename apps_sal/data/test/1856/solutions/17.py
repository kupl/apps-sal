import sys
input = sys.stdin.readline
n = int(input())


def find(x):
    if x != f[x]:
        f[x] = find(f[x])
    return f[x]


f = list(range(n + 26))
for i in range(0, n):
    for j in set(input().rstrip()):
        f[find(ord(j) - 97)] = find(i + 26)
ans = 0
for i in range(26, n + 26):
    if f[i] == i:
        ans += 1
print(ans)
