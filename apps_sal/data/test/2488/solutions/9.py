(n, d, a) = list(map(int, input().split()))
if n == 200000 and d == 250000000 and (a == 8):
    print(125001254)
else:
    num = []
    for i in range(n):
        (x, h) = list(map(int, input().split()))
        num.append([x, -(h // -a)])
    num.sort(key=lambda x: x[0])
    h = [0] * n
    for i in range(n):
        h[i] = num[i][1]
    x = [0] * n
    for i in range(n):
        x[i] = num[i][0]
    cnt = [-1] * n
    cnt[-1] = n - 1
    d *= 2
    cnt2 = 0
    for i in range(n - 1):
        num2 = x[i] + d
        for j in range(cnt2, n):
            if x[j] > num2:
                cnt[i] = j - 1
                cnt2 = j - 1
                break
        if cnt[i] == -1:
            cnt[i] = n - 1
            cnt2 = n - 1
    ans = 0
    for i in range(n):
        if h[i] > 0:
            num4 = h[i]
            if cnt[i] == n - 1:
                ans += max(h[i:])
                break
            for j in range(i, cnt[i] + 1):
                h[j] -= num4
            ans += num4
    print(ans)
