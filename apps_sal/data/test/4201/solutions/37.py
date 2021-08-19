from itertools import product
h, w, k = map(int, input().split())
c = [input() for i in range(h)]
ans = 0

for maskR in product([0, 1], repeat=h):
    for maskC in product([0, 1], repeat=w):
        b = 0
        for i in range(h):
            for j in range(w):
                if maskR[i] == 1 and maskC[j] == 1 and c[i][j] == "#":
                    b += 1
        if b == k:
            ans += 1
print(ans)
