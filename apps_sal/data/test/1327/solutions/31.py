n, m = map(int, input().split())
As = [[] for i in range(8)]
for i in range(n):
    x, y, z = map(int, input().split())
    As[0].append(-x - y - z)
    As[1].append(-x - y + z)
    As[2].append(-x + y - z)
    As[3].append(-x + y + z)
    As[4].append(x - y - z)
    As[5].append(x - y + z)
    As[6].append(x + y - z)
    As[7].append(x + y + z)

ans = 0
for a in As:
    a.sort(reverse=True)
    s = sum(a[:m])
    ans = max(ans, s)
print(ans)
