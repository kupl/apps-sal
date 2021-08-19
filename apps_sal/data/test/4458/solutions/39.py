N = int(input())
P = list(map(int, input().split()))
ans = 0
check = 10 ** 9 + 7
for i in range(N):
    if check > P[i]:
        ans += 1
        check = P[i]
print(ans)
