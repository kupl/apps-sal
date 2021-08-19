N = int(input())
for i in range(N):
    k = int(input())
    a = [int(u) for u in input().split()]
    cc = sum(a)
    if cc == 1:
        ans = (k - 1) * 7 + 1
    else:
        if k % cc == 0:
            ans = (k - cc) // cc * 7
            left = cc
        else:
            ans = k // cc * 7
            left = k % cc
        mini = 10000
        for i in range(7):
            cur = 0
            go = left
            for j in range(7):
                if go == 0:
                    break
                cur += 1
                if a[(i + j) % 7] == 1:
                    go -= 1
            if cur < mini:
                mini = cur
        ans += mini
    print(ans)
