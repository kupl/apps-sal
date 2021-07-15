#aとbどちらが勝つか
def comp(a, b):
    if a=='R' and b=='P': return b
    elif a=='P' and b=='S': return b
    elif a=='S' and b=='R': return b
    else: return a
N, K = map(int, input().split())
S = input()
T = S + S
dp = [[] for i in range(K+1)]
for i in range(2*N):
    dp[0].append(T[i])

for k in range(1,K+1):
    for i in range(N):
        dp[k].append(comp(dp[k-1][2*i], dp[k-1][2*i+1]))
    dp[k] = dp[k]+dp[k]
print(dp[K][0])
