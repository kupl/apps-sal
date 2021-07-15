n = int(input())
route, ans = [], []
for i in range(n-1):
    a = list(map(int, input().split()))
    route.append(a)

for i in range(n-1):
    c = route[i][0]+route[i][1]
    for j in range(i+1, n-1):
        if c < route[j][1]:
            c = route[j][0]+route[j][1]
        elif (c-route[j][1])%route[j][2] == 0:
            c += route[j][0]
        else:
            c += route[j][0]+route[j][2]-(c-route[j][1])%route[j][2]
    ans.append(c)
ans.append(0)
for i in ans:
    print(i)

