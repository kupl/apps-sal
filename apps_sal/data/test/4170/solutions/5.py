N = int(input())
H = list(map(int, input().split()))
ans = 0
tmp = 0
for i in range(1, N):
    if H[i] <= H[i - 1]:
        tmp += 1
        ans = max(ans, tmp)
    else:
        tmp = 0
print(ans)
