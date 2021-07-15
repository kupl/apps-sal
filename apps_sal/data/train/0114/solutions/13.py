t = int(input())
for _ in range(t):
    # print()
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = [tuple(map(int, input().split())) for __ in range(m)]
    ans = 1
    # mx[i] stores the max power of the hero that can go i steps
    mx = [0] * (n + 1)
    for p, s in b:
        mx[s] = max(mx[s], p)
    for i in range(n-1, -1, -1):
        mx[i] = max(mx[i], mx[i+1])

    # print(a)
    # print(b)
    if mx[1] < max(a):
        print(-1)
    else:
        index = 1
        ma = 0
        for mon in a:
            ma = max(mon, ma)
            if mx[index] < ma:
                index = 1
                ans += 1
                ma = mon
            index += 1
        # ind = 0
        # while ind < n:
        #     temp = 0
        #     for i in range(m):
        #         l = 0
        #         if b[i][0] <= temp:
        #             break
        #         if ind + temp == n:
        #             break
        #         # print(a[ind:len(a)])
        #         end = min(ind+b[i][0], len(a))
        #         for j in range(ind, end):
        #             if a[j] > b[i][1]:
        #                 break
        #             l += 1
        #         if l > temp:
        #             temp = l
        #     # print(temp, ind)
        #     ind += temp
        #     ans += 1
        #     # print(a, temp)
        print(ans)

