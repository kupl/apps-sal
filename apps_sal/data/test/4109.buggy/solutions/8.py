(N, M, X) = map(int, input().split())
item = []
ans = []
for i in range(N):
    item.append(list(map(int, input().split())))
for i in range(2 ** N):
    bag = []
    money = 0
    for j in range(N):
        if i >> j & 1:
            bag.append(item[j])
    if bag == []:
        continue
    total = [0] * M
    for k in bag:
        money += k[0]
        for l in range(1, M + 1):
            total[l - 1] += k[l]
    if min(total) >= X:
        ans.append(money)
if ans == []:
    print(-1)
else:
    print(min(ans))
