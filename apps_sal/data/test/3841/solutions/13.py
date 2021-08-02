p, k = map(int, input().split())
r = []
while p:
    r.append(p % k)
    p = -(p // k)
print(len(r))
print(*r, sep=' ')
