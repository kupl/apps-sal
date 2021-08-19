(n, k) = list(map(int, input().split()))
td = sorted([list(map(int, input().split())) for i in range(n)], reverse=True, key=lambda x: x[1])
ans = 0
kl = dict()
for i in range(k):
    ans += td[i][1]
    if td[i][0] in kl:
        kl[td[i][0]] += 1
    else:
        kl[td[i][0]] = 1
l = len(kl)
ans += l ** 2
ans_ = ans
now = k - 1
for i in range(k, n):
    if td[i][0] not in kl:
        while now >= 0:
            if kl[td[now][0]] > 1:
                mi = td[now]
                kl[mi[0]] -= 1
                now -= 1
                break
            now -= 1
        if now == -1:
            break
        else:
            ans = ans + 2 * l + 1 - mi[1] + td[i][1]
            kl[td[i][0]] = 1
            ans_ = max(ans, ans_)
            l += 1
print(ans_)
