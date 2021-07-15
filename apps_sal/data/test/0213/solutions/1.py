n, m = [int(x) for x in input().split()]
data = []
for i in range(m):
    k, f = [int(x) for x in input().split()]
    data.append((k - 1, f - 1))
ans = set()
#tmp = []
for x in range(1, 101):
    for elem in data:
        if elem[0] // x != elem[1]:
            break
    else:
        ans.add((n - 1) // x + 1)
        #tmp.append((n - 1) // x + 1)
if len(ans) == 1:
    print(ans.pop())
else:
    print(-1)
