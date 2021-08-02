n, k = list(map(int, input().split()))
hhh = list(map(int, input().split()))

h = [0] * 200005
hp = [0] * 200005

mx = 0
for i in hhh:
    h[i] += 1
    mx = max(mx, i)

res = n
for j in range(200003):
    hp[j] = res
    res -= h[j]


ans = 0
rr = 0
for t in range(mx, 0, -1):
    if hp[t] == n:
        break

    rr += hp[t]
    if rr > k:
        rr = hp[t]
        ans += 1


if rr:
    ans += 1

print(ans)
