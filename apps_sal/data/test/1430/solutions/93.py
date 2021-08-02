n, k = map(int, input().split())
s = input()
a = []
b = []
c = 0
d = "1"
for i in s:
    if d == i:
        c += 1
    else:
        if d == "1":
            b.append(c)
            d = "0"
            c = 1
        else:
            a.append(c)
            d = "1"
            c = 1
if d == "1":
    b.append(c)
else:
    a.append(c)
    b.append(0)
if k >= len(a):
    print(n)
else:
    e = sum(a[:k]) + sum(b[:k + 1])
    ans = e
    for i in range(len(a) - k):
        e = e - a[i] - b[i] + a[i + k] + b[i + k + 1]
        ans = max(ans, e)
    print(ans)
