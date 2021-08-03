# In the name of Allah

from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
v = a[0]
a = sorted(a[1:], reverse=True)
ans = 0

if len(a) == 1:
    a += [0]

while v <= a[0]:
    v += 1
    ans += 1
    a[0] -= 1
    if a[0] < a[1]:
        a.sort(reverse=True)

stdout.write(str(ans))
