N,M = map(int,input().split())
drink = [list(map(int,input().split())) for _ in range(N)]
drink = sorted(drink)
ans = 0
for i in range(N):
   for j in range(drink[i][1]):
        ans += drink[i][0]
        M -= 1
        if M == 0:
            print(ans)
            return
