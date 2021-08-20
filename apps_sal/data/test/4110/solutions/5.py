import itertools as itr
(D, G) = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(D)]
b = list(itr.product(range(2), repeat=D))
ans = float('INF')
for i in range(len(b)):
    temp = 0
    pnt = 0
    for j in range(D):
        if b[i][j] == 1:
            temp += p[j][0]
            pnt += (j + 1) * 100 * p[j][0]
            pnt += p[j][1]
    if pnt >= G:
        ans = min(ans, temp)
    else:
        for j in range(D):
            if b[i][-j - 1] == 0:
                for k in range(p[-j - 1][0] - 1):
                    temp += 1
                    pnt += (D - j) * 100
                    if pnt >= G:
                        ans = min(ans, temp)
                        break
                break
print(int(ans))
