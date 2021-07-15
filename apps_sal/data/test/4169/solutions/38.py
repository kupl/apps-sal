N, M = map(int, input().split())
AB = [0] * N
for i in range(N):
    AB[i] = list(map(int, input().split()))

AB = sorted(AB, key = lambda x: x[0])
ans = 0

for i in range(N):
    if M > AB[i][1]:
        M -= AB[i][1]
        ans += AB[i][0] * AB[i][1]
    else:
        ans += AB[i][0] * M
        M = 0
    if M == 0:
        break

print(ans)
