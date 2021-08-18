n, m = map(int, input().split())
if m == 0:
    print(0)
    return

res_111 = []
res_110 = []
res_101 = []
res_100 = []
res_011 = []
res_010 = []
res_001 = []
res_000 = []

for i in range(n):
    x, y, z = map(int, input().split())
    res_111.append(x + y + z)
    res_110.append(x + y - z)
    res_101.append(x - y + z)
    res_100.append(x - y - z)
    res_011.append(-x + y + z)
    res_010.append(-x + y - z)
    res_001.append(-x - y + z)
    res_000.append(-x - y - z)

res_111.sort()
res_110.sort()
res_101.sort()
res_100.sort()
res_011.sort()
res_010.sort()
res_001.sort()
res_000.sort()

print(max(sum(res_111[-m:]), sum(res_110[-m:]), sum(res_101[-m:]), sum(res_100[-m:]), sum(res_011[-m:]), sum(res_010[-m:]), sum(res_001[-m:]), sum(res_000[-m:])))
