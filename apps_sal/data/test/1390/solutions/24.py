(N, M) = list(map(int, input().split(' ')))
puzzles = list(map(int, input().split(' ')))
puzzles.sort()
ans = 100000000000
for i in range(N - 1, M):
    ans = min(ans, puzzles[i] - puzzles[i - N + 1])
print(ans)
