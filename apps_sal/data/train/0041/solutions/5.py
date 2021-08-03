t = int(input())
for z in range(t):
    n, k = map(int, input().split())
    arr = list(input())
    need = '()' * (k - 1) + '(' * ((n - (k - 1) * 2) // 2) + ')' * ((n - (k - 1) * 2) // 2)
    # print(need)
    li = 0
    ri = n - 1
    ln = 0
    rn = n - 1
    ret = []
    rev = 0
    while li < n:
        if arr[li] != need[li]:
            ri = li + 1
            while arr[ri] != need[li]:
                ri += 1
            ret.append([li, ri])
            arr = arr[:li] + list(reversed(arr[li:ri + 1])) + arr[ri + 1:]
        li += 1
    #print(*arr, sep='')

    print(len(ret))
    for x in ret:
        print(x[0] + 1, x[1] + 1)
