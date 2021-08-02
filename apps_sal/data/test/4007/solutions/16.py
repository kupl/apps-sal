n = int(input())
f = list(map(int, input().split()))
give = set(i for i in range(n))
get = set(i for i in range(n))
for i in range(n):
    if f[i] > 0:
        give.remove(i)
        get.remove(f[i] - 1)
givel = list(give)
for x in givel:
    if x in get:
        give.remove(x)
        for j in get:
            if j == x:
                continue
            f[x] = j + 1
            break
        get.remove(j)
givel = list(give)
for x in give:
    for j in get:
        f[x] = j + 1
        break
    get.remove(j)
print(' '.join(map(str, f)))
