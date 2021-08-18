def distance(fro, to):
    nonlocal n
    return to - fro if to - fro >= 0 else n + to - fro


n, m = list(map(int, input().split()))
count = [-1 for i in range(n + 1)]
dis = [n for i in range(n + 1)]
ans = []
for i in range(1, m + 1):
    a, b = list(map(int, input().split()))
    dis[a] = min(distance(a, b), dis[a])
    count[a] += 1
#    print(a,count[a])
#    print(dis[a],a,n,b)
for i in range(1, n + 1):
    dis[i] = dis[i] + n * count[i]
#    print(dis[i],count[i],i)
# print(dis)
for i in range(1, n + 1):
    ans.append(max([dis[k] + distance(i, k) if dis[k] > 0 else 0 for k in range(1, n + 1)]))
print(*ans)
