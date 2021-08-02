n = int(input())
a = []
S = 0

for i in range(n):
    a.append(tuple(map(int, input().split())))
for i in range(n):
    for j in range(n):
        S = max(S, abs((a[i][0] - a[j][0]) * (a[i][1] - a[j][1])))

if S == 0:
    print(-1)
else:
    print(S)
