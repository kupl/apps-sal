N, K = [int(n) for n in input().split()]
ans = 0
for n in range(1, N+1):
    tmp = 1.0/N
    now = n
    while now < K:
        now *=2
        tmp /=2
    ans += tmp
print(('{:.12}'.format(ans)))

