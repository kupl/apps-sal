import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

MOD = 10**9 + 7

N, K = list(map(int, input().split()))
adjL = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1
    adjL[a].append(b)
    adjL[b].append(a)

nums = [1] * N
def dfs(vNow, vPar):
    numCh = 0
    for v2 in adjL[vNow]:
        if v2 == vPar: continue
        dfs(v2, vNow)
        numCh += 1
    num = 1
    if vPar == -1:
        for i in range(K-numCh, K):
            num *= i
            num %= MOD
    else:
        for i in range(K-numCh-1, K-1):
            num *= i
            num %= MOD
    nums[vNow] = num

dfs(0, -1)

ans = K
for num in nums:
    ans *= num
    ans %= MOD

print(ans)

