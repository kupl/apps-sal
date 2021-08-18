N = int(input())
H = list(map(int, input().split()))

ans, tmp = 0, 0
for i in range(N - 1):
    if H[i] >= H[i + 1]:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0

ans = max(ans, tmp)
print(ans)
