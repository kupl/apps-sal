N, K, M = map(int, input().split())
score = list(map(int, input().split()))
for i in range(K + 1):
    if (sum(score) + i) / N >= M:
        print(i)
        return
print(-1)
