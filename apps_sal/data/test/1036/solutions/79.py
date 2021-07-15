# 先頭プレイヤーがS[offset]で始まる部分トーナメントを考える
# 2^k人の勝者を予想する。
N, K = map(int, input().split())
S = input()
dp = [['?']*(N+1) for i in range(K+1)]
def memo(k, i):
    if k==0: return S[i]
    if dp[k][i]!='?': return dp[k][i]
    ni=(i+2**(k-1))%N
    res = Win(memo(k-1,i), memo(k-1, ni))
    dp[k][i] = res
    return dp[k][i]

def Win(a, b):
    if a=='R' and b=='P': return b
    elif a=='P' and b=='S': return b
    elif a=='S' and b=='R': return b
    else: return a
ans = memo(K, 0)
print(ans)
