N = int(input())
P = list(map(int, input().split()))
ans = N
min_val = N
for i in range(N):
    target = P[i]
    if target < min_val:
        min_val = target
    if min_val < target:
        ans -= 1
print(ans)
