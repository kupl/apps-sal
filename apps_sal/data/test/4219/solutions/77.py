n = int(input())
(al, xyl) = ([], [])
for _ in range(n):
    a = int(input())
    xy = [list(map(int, input().split())) for _ in range(a)]
    xyl.append(xy)
ans = 0
for i in range(2 ** n):
    cnt = 0
    flag = True
    for j in range(n):
        if i >> j & 1:
            cnt += 1
            for (x, y) in xyl[j]:
                x -= 1
                if i >> x & 1 != y:
                    flag = False
    if flag:
        ans = max(ans, cnt)
print(ans)
