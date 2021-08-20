n = int(input())
xy = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        (x_, y_) = map(int, input().split())
        xy[i].append((x_ - 1, y_))
ans = 0
for i in range(1, 2 ** n):
    flag = 0
    for j in range(n):
        if i >> j & 1:
            for (x, y) in xy[j]:
                if i >> x & 1 != y:
                    flag = 1
                    break
    if flag == 0:
        ans = max(ans, bin(i)[2:].count('1'))
print(ans)
