n, v = map(int, input().split())
p = 0
q = []
for i in range(n):
    k = list(map(int, input().split()))
    km = min(k[1:])
    if km < v:
        p += 1
        q.append(i+1)

print(p)
for x in q:
    print(x, end=' ')


