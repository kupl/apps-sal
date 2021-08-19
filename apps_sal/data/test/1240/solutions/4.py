n = int(input())
(L, R) = (0, 0)
a = []
for i in range(n):
    (li, ri) = map(int, input().split())
    a.append([li, ri])
    L += li
    R += ri
ans = abs(L - R)
ansi = 0
for i in range(n):
    l1 = L - a[i][0] + a[i][1]
    r1 = R - a[i][1] + a[i][0]
    if abs(l1 - r1) > ans:
        ans = abs(l1 - r1)
        ansi = i + 1
print(ansi)
