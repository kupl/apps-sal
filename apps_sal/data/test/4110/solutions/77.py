(D, G) = map(int, input().split())
G /= 100
P = []
C = []
for _ in range(D):
    (x, y) = map(int, input().split())
    P.append(x)
    C.append(y // 100)
ans = 10 ** 9
for x in range(2 ** D):
    cost = 0
    value = 0
    for i in range(D):
        if (x >> i) % 2 == 1:
            value += P[i] * (i + 1) + C[i]
            cost += P[i]
    for i in range(D - 1, -1, -1):
        if value >= G:
            break
        elif (x >> i) % 2 == 0:
            for _ in range(P[i] - 1):
                value += i + 1
                cost += 1
                if value >= G:
                    break
    if value >= G:
        ans = min(ans, cost)
print(ans)
