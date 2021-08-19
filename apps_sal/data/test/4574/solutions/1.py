N = int(input())
data = list(map(int, input().split()))
data.sort()
ans = []
N -= 1
while N > 0:
    if data[N] == data[N - 1]:
        ans.append(data[N])
        N -= 1
    N -= 1
    if len(ans) >= 2:
        break
if len(ans) < 2:
    print(0)
else:
    print(ans[0] * ans[1])
