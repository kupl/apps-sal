n, k, m, t = list(map(int, input().split()))
for _ in range(t):
    c, i = list(map(int, input().split()))
    if(c == 1):
        n += 1
        if(i <= k):
            k += 1
    if(c == 0):
        if(i < k):
            k -= i
            n -= i
        else:
            n = i
    print(n, k)
