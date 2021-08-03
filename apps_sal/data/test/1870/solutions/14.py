N, C = list(map(int, input().split()))
T = list(map(int, input().split()))
ans = 1
for i in range(1, N):
    if T[i] - T[i - 1] > C:
        ans = 1
    else:
        ans += 1
print(ans)
