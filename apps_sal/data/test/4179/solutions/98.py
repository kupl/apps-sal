(N, M, C) = map(int, input().split())
list_b = list(map(int, input().split()))
ans = 0
for i in range(N):
    temp = 0
    list_a = list(map(int, input().split()))
    for j in range(M):
        temp += list_a[j] * list_b[j]
    if temp + C > 0:
        ans += 1
print(ans)
