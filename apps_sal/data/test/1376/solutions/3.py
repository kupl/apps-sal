n = int(input())
a = list(map(int, input().split()))
res = [[] for i in range(n)]
for i in range(2 * n):
    res[a[i] - 1].append(i)
last1 = 0
last2 = 0
su = 0
for i in range(n):
    su += min(abs(last1 - res[i][0]) + abs(last2 - res[i][1]), abs(last1 - res[i][1]) + abs(last2 - res[i][0]))
    last1 = res[i][0]
    last2 = res[i][1]
print(su)
