n, k, m, t = map(int, input().split())
for i in range(t):
    type, i = map(int, input().split())
    if type:
        n += 1
        if k >= i:
            k += 1
    else:
        if k >= i + 1:
            k -= i
            n -= i
        else:
            n = i
    print(n, k)
