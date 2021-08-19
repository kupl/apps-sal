[n, A] = [int(x) for x in input().split()]
d = [0] + [int(x) for x in input().split()]
sigma = sum(d)
ans = [0] * (n + 1)
for i in range(1, n + 1):
    at_least = A - sigma + d[i] - 1
    at_least = max(at_least, 0)
    ans[i] += at_least
    at_most = d[i] - A + n - 1
    at_most = max(at_most, 0)
    ans[i] += at_most
ans = ans[1:]
ans = [str(x) for x in ans]
print(' '.join(ans))
