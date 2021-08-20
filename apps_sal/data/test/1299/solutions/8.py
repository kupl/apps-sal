(n, k) = map(int, input().split())
a = list(map(int, input().split()))
sums = [0]
for x in a:
    sums.append(x + sums[-1])
S = l = r = ans = pos = 0
for i in range(k, n - k + 1):
    (prev, cur, nex) = (sums[i - k], sums[i], sums[i + k])
    dif = cur - prev
    if dif > S:
        S = dif
        pos = i - k
    dif = nex - cur
    if S + dif > ans:
        ans = S + dif
        l = pos
        r = i
print(l + 1, r + 1)
