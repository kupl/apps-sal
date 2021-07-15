n, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
s = 0
for i in range(k):
    s += p[i]
print(s)
