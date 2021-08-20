(n, k) = [int(x) for x in input().split()[:2]]
an = [int(x) for x in input().split()[:n]]
tn = [int(x) for x in input().split()[:n]]
first = 0
for i in range(k):
    first += an[i]
for i in range(k, n):
    first += an[i] * tn[i]
ans = first
for i in range(1, n - k + 1):
    new = i + k - 1
    last = i - 1
    if tn[last] == 0:
        first -= an[last]
    if tn[new] == 0:
        first += an[new]
    ans = max(first, ans)
print(ans)
