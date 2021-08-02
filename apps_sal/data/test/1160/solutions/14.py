d = {"S": 0, "M": 1, "L": 2, "XL": 3, "XXL": 4, "XXXL": 5}

cnt = [int(t) for t in input().split()]
n = int(input())
ind = [i for i in range(n)]
p = []
for i in range(n):
    p.append(input().split(','))
ind.sort(key=lambda x: [d[p[x][0]], len(p[x])])
ans = {}
for i in ind:
    cur = p[i]
    if cnt[d[cur[0]]] != 0:
        ans[i] = cur[0]
        cnt[d[cur[0]]] -= 1
    elif len(cur) == 2 and cnt[d[cur[1]]] != 0:
        ans[i] = cur[1]
        cnt[d[cur[1]]] -= 1
    else:
        print("NO")
        return
print("YES")
for i in ans.keys():
    print(ans[i])
