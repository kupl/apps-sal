S = input()
Q = int(input())
Query = list(input().split() for _ in range(Q))

count = 0
L, R = "", ""

for i in range(Q):
    if Query[i][0] == "1": count += 1
    else:
        if Query[i][1] == "1":
            if count % 2 == 0: L = Query[i][2] + L
            else: R += Query[i][2]
        else:
            if count % 2 == 0: R += Query[i][2]
            else: L = Query[i][2] + L

if count % 2 == 0: print(L + S + R)
else: print(R[::-1] + S[::-1] + L[::-1])
