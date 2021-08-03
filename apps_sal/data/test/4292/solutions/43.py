n, k = list(map(int, input().split()))

p = list(map(int, input().split()))

ans = 0

l = list()

for i in range(k):
    l.append(min(p))
    p.remove(min(p))

ans = sum(l)

print(ans)
