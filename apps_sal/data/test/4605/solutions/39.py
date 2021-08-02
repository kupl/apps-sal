N, A, B = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    k = list(str(i))
    sum_i = 0
    for j in k:
        sum_i += int(j)
    if A <= sum_i <= B:
        ans += i

print(ans)
