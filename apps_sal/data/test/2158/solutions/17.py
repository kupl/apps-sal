n = int(input())
dicts = {}
for i in range(n - 1):
    temparr = input()
    temparr = temparr.split()
    u = int(temparr[0])
    v = int(temparr[1])
    weight = int(temparr[2])

    if u not in dicts:
        dicts[u] = []
    dicts[u].append((v, weight))

    if v not in dicts:
        dicts[v] = []
    dicts[v].append((u, weight))
maxans = 0


def dfs(cur, par=-1, sums=0):
    nonlocal dicts
    nonlocal maxans
    for element in dicts[cur]:
        nextelement = element[0]
        nextweight = element[1]
        if par != nextelement:
            sums += nextweight
            if maxans <= sums:
                maxans = sums
            dfs(nextelement, cur, sums)
            sums -= nextweight


dfs(0, -1, 0)
print(maxans)
print()

# void dfs(int cur , int par = -1)
# {
#   // do what u want
#   for(auto x : g[cur])
#   {
#     if(x!=par)
#     {
#       dfs(x,cur);
#     }
#   }
# }

# print(dicts)
