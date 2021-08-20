def read():
    return list(map(int, input().split()))


n = int(input())
(l, r) = ([0] * n, [0] * n)
L = R = 0
for i in range(n):
    (l[i], r[i]) = read()
    L += l[i]
    R += r[i]
Max = abs(L - R)
ans = 0
for i in range(n):
    cur = abs(L - l[i] + r[i] - (R - r[i] + l[i]))
    if cur > Max:
        Max = cur
        ans = i + 1
print(ans)
