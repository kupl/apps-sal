n = int(input())
li = list(map(int, input().split()))
if n == 1:
    print(-1)
elif n == 2:
    li.sort()
    d = li[1] - li[0]
    if d == 0:
        print(1)
        print(li[0])
    elif d % 2 == 0:
        print(3)
        print(li[0] - d, li[0] + d // 2, li[1] + d)
    else:
        print(2)
        print(li[0] - d, li[1] + d)
else:
    flag = 0
    li.sort()
    d = li[1] - li[0]
    for i in range(2, n):
        if li[i] - li[i - 1] < d:
            d = li[i] - li[i - 1]
    for i in range(1, n):
        if li[i] - li[i - 1] != d:
            if li[i] - li[i - 1] == 2 * d:
                flag += 1
                ind = i
            else:
                flag = -1
                break
    if d == 0 and flag == 0:
        print(1)
        print(li[0])
    elif flag == -1 or flag > 1:
        print(0)
    elif flag == 1:
        print(1)
        print(li[ind] - d)
    else:
        print(2)
        print(li[0] - d, li[-1] + d)
