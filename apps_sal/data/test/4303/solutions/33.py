(n, k) = map(int, input().split())
x = list(map(int, input().split()))
neg_to_pos = n
for i in range(n):
    if x[i] > 0:
        neg_to_pos = i
        break
res = 10 ** 14
for i in range(n - k + 1):
    l = min(x[i], 0)
    r = max(0, x[i + k - 1])
    if i <= neg_to_pos and neg_to_pos - 1 <= i + k - 1:
        tmp = min(-2 * l + r, -l + 2 * r)
        res = min(res, tmp)
print(res)
