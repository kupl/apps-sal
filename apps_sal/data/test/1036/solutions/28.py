N, K = list(map(int, input().split()))
S = input()

def judge(a, b):
    win = a
    if a+b == "RP":
        win = b
    elif a+b == "PS":
        win = b
    elif a+b == "SR":
        win = b
    return win

memo = [[""] * (N+5) for _ in range(K+5)]
def rec(k, i):
    if memo[k][i]: return memo[k][i]
    if k == 0:
        ret = judge(S[i%N], S[(i+1)%N])
        memo[k][i] = ret
        return ret
    win = judge(rec(k-1, i%N), rec(k-1, (i+pow(2,k,N))%N))
    memo[k][i] = win
    return win

ans = rec(K-1, 0)
print(ans)

