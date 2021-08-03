N, K, M = map(int, input().split())
A = list(map(int, input().split()))
ans = max(0, M * N - sum(A))
ans = ans if ans <= K else -1
print(ans)
