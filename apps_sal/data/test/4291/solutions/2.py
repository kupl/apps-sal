n, q = map(int, input().split())
s = list(input())
a = [0] * n
r = 0
for ii in range(n - 1):
    if s[ii] == "A" and s[ii + 1] == "C":
        r += 1
    a[ii] = r
for _ in range(q):
    l, r = map(int, input().split())
    print(a[r - 2] - a[l - 2])
