n, n1, n2 = map(int, input().split())
p = list(map(int, input().split()))
n1, n2 = min(n1, n2), max(n1, n2)
p.sort(reverse=True)
res1 = 0
res2 = 0
#print(p)
for i in range(n1 + n2):
    if i < n1:
        res1 += p[i]
    else:
        res2 += p[i]
#print(res1, res2)
print(res1/n1 + res2/n2)
