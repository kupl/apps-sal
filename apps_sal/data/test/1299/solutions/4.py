n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
sums = []
for x in a: sums.append(x + sums[-1] if x > 0 else 0)
S = l = r = ans = pos = 0
for i in range(k + 1, n - k + 2):
    if sums[i - 1] - sums[i - k - 1] > S:
        S = sums[i - 1] - sums[i - k - 1]
        pos = i - k
    if S + sums[i + k - 1] - sums[i - 1] > ans:
        ans = S + sums[i + k - 1] - sums[i - 1]
        l = pos
        r = i
print(l, r)
