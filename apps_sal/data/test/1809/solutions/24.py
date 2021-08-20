(n, m) = list(map(int, input().split()))
w = list(map(int, input().split()))
l = list(map(int, input().split()))
k = 0
f = []
for x in l:
    x -= 1
    if x not in f:
        for y in f:
            k += w[y]
        f = [x] + f
    else:
        for i in range(len(f)):
            if f[i] != x:
                k += w[f[i]]
            else:
                break
        del f[i]
        f = [x] + f
print(k)
