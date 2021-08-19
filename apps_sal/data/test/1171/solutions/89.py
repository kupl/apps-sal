(N, M) = list(map(int, input().split()))
l = list(map(int, input().split()))
S = min(M, N)
ans = 0
for i in range(S + 1):
    for j in range(S - i + 1):
        mem = l[0:i] + l[N - j:]
        for k in range(min(M - i - j, len(mem))):
            if min(mem) < 0:
                mem.remove(min(mem))
        ans = max(ans, sum(mem))
print(ans)
