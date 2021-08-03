n, k, m, t = list(map(int, input().split()))
for tt in range(t):
    op, i = list(map(int, input().split()))
    if op == 1:
        if i <= k:
            k += 1
        n += 1
    elif op == 0:
        if i < k:
            k -= i
            n -= i
        else:
            n -= n - i
    print(n, k)
