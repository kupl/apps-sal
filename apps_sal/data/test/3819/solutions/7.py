from sys import stdin, exit
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

p = [0] * (n + 1)

for i in a:
    p[i] = 0

for i, v in enumerate(b):
    p[v] = i + 1

ans = 0
if p[1] > 0:

    i = 2
    while i <= n and p[i] == p[i - 1] + 1:
        i += 1
    if p[i - 1] == n:
        j = i
        while j <= n and p[j] <= j - i:
            j += 1
        if j == n + 1:
            print(p[1] - 1)
            return

ans = max([p[i] - i + 1 + n for i in range(1, n + 1)])
print(ans)

