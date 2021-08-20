from sys import stdin
input = stdin.readline
(n, m) = map(int, input().split())
a = []
for x in range(n):
    a.append(input().rstrip())
if n == 1:
    print(0)
elif n >= 4:
    print(-1)
elif n == 2:
    (cnt1, cnt2) = (0, 0)
    for x in range(m):
        if x % 2 == 0:
            cnt1 += a[0][x] == a[1][x]
            cnt2 += a[0][x] != a[1][x]
        else:
            cnt1 += a[0][x] != a[1][x]
            cnt2 += a[0][x] == a[1][x]
    print(min(cnt1, cnt2))
elif n == 3:
    (cnt1, cnt2, cnt3, cnt4) = (0, 0, 0, 0)
    for x in range(m):
        if x % 2 == 0:
            if a[0][x] == a[1][x] == a[2][x]:
                cnt1 += 0
            else:
                cnt1 += 1
            if a[0][x] == a[2][x] and a[0][x] != a[1][x]:
                cnt2 += 0
            else:
                cnt2 += 1
        else:
            if a[0][x] == a[2][x] and a[0][x] != a[1][x]:
                cnt1 += 0
            else:
                cnt1 += 1
            if a[0][x] == a[1][x] == a[2][x]:
                cnt2 += 0
            else:
                cnt2 += 1
        if x % 2 == 0:
            if a[0][x] == a[1][x] and a[0][x] != a[2][x]:
                cnt3 += 0
            else:
                cnt3 += 1
            if a[1][x] == a[2][x] and a[0][x] != a[1][x]:
                cnt4 += 0
            else:
                cnt4 += 1
        else:
            if a[1][x] == a[2][x] and a[0][x] != a[1][x]:
                cnt3 += 0
            else:
                cnt3 += 1
            if a[0][x] == a[1][x] and a[0][x] != a[2][x]:
                cnt4 += 0
            else:
                cnt4 += 1
    print(min(cnt1, cnt2, cnt3, cnt4))
