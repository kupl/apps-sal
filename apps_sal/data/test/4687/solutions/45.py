N, K = map(int, input().split())
ans = []

for i in range(N):
    ab = list(map(int, input().split()))
    ans.append(ab)

ans.sort()

l = 0

for i in range(N):
    l += ans[i][1]
    if l >= K:
        s = i
        break
print(ans[s][0])
