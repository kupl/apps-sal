n = int(input())
b = list(map(int, input().split()))
a = [[b[i], i] for i in range(n)]
a.sort()
ans = [0] * n
cur = 0
num = 1
while cur < n:
    nec = a[cur][0]
    ng = False
    for i in range(n - nec):
        if cur + i >= n:
            ng = True
            break
        elif a[cur + i][0] != a[cur][0]:
            ng = True
            break
        else:
            ans[a[cur + i][1]] = num
    if ng:
        print('Impossible')
        break
    num += 1
    cur += n - nec
else:
    print('Possible')
    print(*ans)
