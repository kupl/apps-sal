(n, k) = [int(x) for x in input().split()]
mas = [int(x) for x in input().split()]
dictyCount = {}
dictyAns = {}
ans = 0
for x in mas[::-1]:
    ans += dictyAns.get(x * k, 0)
    dictyAns[x] = dictyAns.get(x, 0) + dictyCount.get(x * k, 0)
    dictyCount[x] = dictyCount.get(x, 0) + 1
print(ans)
