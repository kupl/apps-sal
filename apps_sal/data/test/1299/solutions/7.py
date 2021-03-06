(n, k) = map(int, input().split())
a = list(map(int, input().split()))
sums = [0]
for x in a:
    sums.append(x + sums[-1])
S = l = r = ans = pos = 0
for i in range(k, n - k + 1):
    (prev, cur, nex) = (sums[i - k], sums[i], sums[i + k])
    if cur - prev > S:
        S = cur - prev
        pos = i - k
    if S + nex - cur > ans:
        ans = S + nex - cur
        l = pos
        r = i
print(l + 1, r + 1)
