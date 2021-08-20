n = int(input())
arr = map(int, input().split())
res = 0
for x in arr:
    res = res + x % 2
finalres = min(n - res, res)
res = res - finalres
finalres = finalres + res // 3
print(finalres)
