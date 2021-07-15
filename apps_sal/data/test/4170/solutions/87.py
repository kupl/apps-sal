N = int(input())
H = list(map(int, input().split()))
num = H[0]
ans = 0
tmp = 0
for i in range(1, N):
    if num >= H[i]:
        tmp += 1
    else:
        tmp = 0
    ans = max(ans, tmp)
    num = H[i]

print(ans)

