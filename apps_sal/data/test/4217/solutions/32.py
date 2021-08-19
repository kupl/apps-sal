(N, M) = map(int, input().split())
foods = [0] * M
for i in range(N):
    KA = list(map(int, input().split()))
    for a in KA[1:]:
        foods[a - 1] += 1
cnt = 0
for j in foods:
    if j == N:
        cnt += 1
print(cnt)
