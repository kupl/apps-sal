stones = list(map(int, input().split()))
scores = []
for i in range(14):
    full = stones[i] // 14
    part = stones[i] % 14
    result = [(stones[j] if i != j else 0) + full for j in range(14)]
    for j in range(i + 1, i + part + 1):
        result[j % 14] += 1
    scores.append(sum((r for r in result if r % 2 == 0)))
print(max(scores))
