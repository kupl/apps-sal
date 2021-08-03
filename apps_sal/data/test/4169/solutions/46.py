N, M = map(int, input().split())
lsd = []
for i in range(N):
    lsd.append(list(map(int, input().split())))
lsd.sort(key=lambda x: x[0])
ans = 0
i = 0
while M != 0:
    if M >= lsd[i][1]:
        ans += lsd[i][0] * lsd[i][1]
        M -= lsd[i][1]
    else:
        ans += lsd[i][0] * M
        M = 0
    i += 1
print(ans)
