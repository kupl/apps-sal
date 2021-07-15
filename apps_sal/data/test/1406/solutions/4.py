n,k,d = map(int, input().split())
if (n > k ** d):
    print(-1)
    return
for i in range(d):
    power = k**i
    resArray = [((j // power) % k +1) for j in range(n)]
    print(' '.join(map(str,resArray)))
