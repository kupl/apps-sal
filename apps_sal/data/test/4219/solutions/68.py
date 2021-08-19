N = int(input())
xy = [[] for i in range(N)]
for i in range(N):
    A = int(input())
    for j in range(A):
        (x, y) = map(int, input().split())
        xy[i].append([x, y])
ans = 0
for i in range(2 ** N):
    b = format(i, '0' + str(N) + 'b')
    t = 0
    f = 0
    for j in range(N):
        if b[j] == '1':
            t += 1
            for k in xy[j]:
                if str(k[1]) != b[k[0] - 1]:
                    f = 1
                    break
    if f == 0:
        ans = max(ans, t)
print(ans)
