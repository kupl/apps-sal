n = int(input())
H = list(map(int, input().split()))

now = H[0]
cnt = 0
ans = 0

for i in range(1,n):
    if now >= H[i]:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0

    now = H[i]

print(max(ans,cnt))
