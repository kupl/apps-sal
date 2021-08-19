def split():
    return list(map(int, input().split()))


(a, b) = split()
candies = split()
p = q = 0
for x in range(a):
    p += candies[x]
    s = min(8, p)
    p -= s
    q += s
    if q >= b:
        print(x + 1)
        break
else:
    print(-1)
