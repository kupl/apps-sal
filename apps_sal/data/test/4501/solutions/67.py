n, a = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
dp = list([0]*(n*a+1) for _ in range(n+1))#動的計画法で解く
dp[0][0] = 1
for x in l:
    for i in range(n, 0, -1):#下行から順に格納していく(上からだと格納したばかりの値が参照されてしまう)
        for j in range(n*a+1):
            if x > j:
                continue
            dp[i][j] += dp[i-1][j-x]

for i in range(n):
    ans += dp[i+1][(i+1)*a]

print(ans)
