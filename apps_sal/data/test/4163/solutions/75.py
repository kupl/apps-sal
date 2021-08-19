n = int(input())
dl = []
ans = 0
f = 0
for _ in range(n):
    din = list(map(int, input().split()))
    dl.append([din[0], din[1]])
for i in range(n - 2):
    if dl[i][0] == dl[i][1] and dl[i + 1][0] == dl[i + 1][1] and (dl[i + 2][0] == dl[i + 2][1]):
        f = 1
        break
if f == 1:
    print('Yes')
else:
    print('No')
