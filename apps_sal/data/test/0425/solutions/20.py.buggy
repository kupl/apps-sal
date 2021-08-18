def bn(x):
    b = []
    i = 1
    j = 0
    while j < 32:
        #print(x & i, x, i)
        b.append(int(x & i != 0))
        i = i << 1
        j += 1
    b.reverse()
    return sum(b)


n, p = list(map(int, input().split()))
for i in range(1, 32):
    bi = bn(n - i * p)
    if bi <= i <= n - i * p:
        print(i)
        return
print(-1)
