n = int(input())
a = list(map(int, input().split()))
s = 0
r = 0
i = 0
k = 1
f = 0
while s != n:
    if a[i] <= s:
        s += 1
        a[i] = 9999
    if s != n and (i == n - 1 or (i == 0 and f)):
        r += 1
        k *= -1
        f = 1
    i += k
print(r)
