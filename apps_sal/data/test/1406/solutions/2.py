n,k,d = map(int, input().split())
if (n > k ** d):
    print(-1)
    return
for i in range(d):
    power = k**i
    resArray = [((j // power) % k +1) for j in range(n)]
    #for j in range(n//(k**i)+1):
    #    resArray.extend([(j % k) + 1] * (k ** i))
    print(' '.join(map(str,resArray)))
