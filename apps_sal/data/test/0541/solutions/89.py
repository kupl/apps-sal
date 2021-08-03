from operator import itemgetter
n, m = map(int, input().split())
lis = []
for _ in range(m):
    lis.append(list(map(int, input().split())))
lis.sort(key=itemgetter(1))
ans = 0
last = 0
for i in range(m):
    if last <= lis[i][0]:
        ans += 1
        last = lis[i][1]
print(ans)
