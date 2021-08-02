from itertools import product
n = int(input())
k = int(input())


pr = list(product([0, 1], repeat=n))

ans = float('inf')
for p in pr:

    tmp = 1
    for i in p:
        if i == 0:
            tmp *= 2
        else:
            tmp += k

    ans = min(ans, tmp)


print(ans)
