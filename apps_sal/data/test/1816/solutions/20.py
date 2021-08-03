import sys
if False:
    inp = open('A.txt', 'r')
else:
    inp = sys.stdin

n = int(inp.readline())
sectors = list(zip(list(map(int, inp.readline().split())), [x + 1 for x in range(n)]))

sectors.sort(key=lambda x: x[0])
ans = 0
for i in range(n - 1):
    ans += max(sectors[i][1] - sectors[i + 1][1], sectors[i + 1][1] - sectors[i][1])
print(ans)
