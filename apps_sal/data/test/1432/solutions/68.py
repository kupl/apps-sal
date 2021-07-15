n = int(input())
data = list(map(int, input().split()))
ans = [0]
for idx, a in enumerate(data):
    if idx%2 == 0:
        ans[0] += a
    else:
        ans[0] -= a

for i in range(n-1):
    dam = data[i]
    score = 2*dam - ans[-1]
    ans.append(score)

print(*ans)
