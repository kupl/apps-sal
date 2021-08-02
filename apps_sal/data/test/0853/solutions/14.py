n = int(input())
m = list(map(int, input().split()))
if 0 in m:
    if 5 in m:
        k = 0
        l = 0
        for i in range(n):
            k += m[i]
            if m[i] == 0:
                l += 1
        p = k // 9
        # print(p)
        p1 = p // 5
        # print(p1)
        if p1 != 0:
            print('5' * p1 * 9 + '0' * l)
        else:
            print(0)
    else:
        print(0)
else:
    print(-1)
