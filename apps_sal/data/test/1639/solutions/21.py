# In the name of Allah

from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = [float("inf")] + list(map(int, input().split()))

ans = 1
t = 1

for i in range(1, n + 1):
    if a[i] < a[i - 1]:
        ans = max(ans, t)
        t = 1
    else:
        t += 1

stdout.write(str(max(ans, t)))
