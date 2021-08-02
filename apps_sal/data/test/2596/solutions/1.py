n, k, m, t = map(int, input().split())
l = n
for i in range(t):
    a, b = map(int, input().split())
    if(a == 0):
        if(b < k):
            l = l - b
            k = k - b
        else:
            l = b
    else:
        l += 1
        if(b <= k):
            k += 1
    print(l, k)
