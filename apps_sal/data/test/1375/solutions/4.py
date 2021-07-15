n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in a[1:]:
    b.append(b[-1] + i)
d = [a[-1]]
for i in a[:-1][::-1]:
    d.append(d[-1] + i)
d = d[::-1]
c = [0] * n
s = b[n - 1]

if b[0] * 3 == s:
    c[0] = 1
for i in range(1, n):
    if b[i] * 3 == s:
        c[i] = c[i - 1] + 1
    else:
        c[i] = c[i - 1]

ans = 0
for i in range(2, n):
    if d[i] * 3 == s:
        ans = ans + c[i - 2]

print(ans)
