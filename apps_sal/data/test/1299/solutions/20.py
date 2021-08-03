n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
sums = [0]
for x in a:
    sums.append(x + sums[-1])
S = l = r = ans = pos = 0
for i in range(k, n - k + 1):
    if sums[i] - sums[i - k] > S:
        S = sums[i] - sums[i - k]
        pos = i - k
    if S + sums[i + k] - sums[i] > ans:
        ans = S + sums[i + k] - sums[i]
        l = pos
        r = i
print(l + 1, r + 1)
