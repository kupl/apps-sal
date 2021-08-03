from bisect import bisect_left
n, m = map(int, input().split())

l = [[] for _ in range(n)]
city = []
for i in range(m):
    p, y = map(int, input().split())
    city.append([p, y])
    l[p - 1].append(y)

for i in l:
    i.sort()
for i in city:
    ans = ""
    ans += "0" * (6 - len(str(i[0]))) + str(i[0])
    t = str(bisect_left(l[i[0] - 1], i[1]) + 1)
    ans += "0" * (6 - len(t)) + t
    print(ans)
