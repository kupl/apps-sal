(N, A, B) = map(int, input().split())
ans = []
for i in range(1, N + 1):
    j = i // 10000 + i % 10000 // 1000 + i % 1000 // 100 + i % 100 // 10 + i % 10 // 1
    if A <= j <= B:
        ans.append(i)
print(sum(ans))
