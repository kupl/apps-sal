def dfs(seq):
    ans = 0
    if len(seq) == n:
        kou = 0
        for u in data:
            if seq[u[1]-1] - seq[u[0]-1] == u[2]:
                kou+=u[3]
        return kou
    else:#len(seq)==N-1からの遷都を考えると良い
        for i in range(seq[-1], m+1):
            seq_next=seq+[i]
            ans = max(ans, dfs(seq_next))
        return ans

n, m, q = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(q)]

score = dfs([1])
print(score)

