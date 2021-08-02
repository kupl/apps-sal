N = int(input())
P = list(map(int, input().split()))

tmp = N
cnt = 0
for i in range(N):
    tmp = min(tmp, P[i])
    if tmp >= P[i]:
        cnt += 1
print(cnt)
