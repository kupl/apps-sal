import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

N,K = list(map(int,input().split()))
A = list(map(int,input().split()))

def is_divide(d):
    Rs = [a%d for a in A]
    Rs.sort()
    cumsum = [0] * (N + 1)
    for i in range(N - 1,-1,-1):
        cumsum[i] = cumsum[i + 1] + d - Rs[i]
    cum = 0
    for i in range(N):
        if max(cum,cumsum[i]) <= K:
            return True
        cum += Rs[i]
    return False

S = sum(A)
ans = 0
for i in range(1,S + 1):
    if i*i > S:
        break
    if S%i == 0:
        if is_divide(i):
            ans = max(ans,i)
        if is_divide(S//i):
            ans = max(ans,S//i)
print(ans)

