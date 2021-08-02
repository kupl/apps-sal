

shorts = [int(t) for t in input().split()]
n = int(input())
d = dict()
d["S"] = 0
d["M"] = 1
d["L"] = 2
d["XL"] = 3
d["XXL"] = 4
d["XXXL"] = 5
people = []
order = [t for t in range(n)]
for _ in range(n):
    people.append(input().split(","))
order.sort(key=lambda x: [d[people[x][0]], len(people[x])])
ans = dict()
for i in order:
    p = people[i]
    if shorts[d[p[0]]] != 0:
        ans[i] = p[0]
        shorts[d[p[0]]] -= 1
    elif len(p) == 2 and shorts[d[p[1]]] != 0:
        ans[i] = p[1]
        shorts[d[p[1]]] -= 1
    else:
        print("NO")
        return
print("YES")
for i in ans.keys():
    print(ans[i])
