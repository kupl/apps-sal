(n, m) = map(int, input().split())
cake = [[int(i) for i in input().split()] for j in range(n)]
a = sum(sorted([sum(i) for i in cake], reverse=True)[:m])
b = sum(sorted([cake[i][0] + cake[i][1] - cake[i][2] for i in range(n)], reverse=True)[:m])
c = sum(sorted([cake[i][0] - cake[i][1] - cake[i][2] for i in range(n)], reverse=True)[:m])
d = sum(sorted([cake[i][0] - cake[i][1] + cake[i][2] for i in range(n)], reverse=True)[:m])
e = sum(sorted([0 - cake[i][0] + cake[i][1] - cake[i][2] for i in range(n)], reverse=True)[:m])
f = sum(sorted([0 - cake[i][0] + cake[i][1] + cake[i][2] for i in range(n)], reverse=True)[:m])
g = sum(sorted([0 - cake[i][0] - cake[i][1] - cake[i][2] for i in range(n)], reverse=True)[:m])
h = sum(sorted([0 - cake[i][0] - cake[i][1] - cake[i][2] for i in range(n)], reverse=True)[:m])
print(max(a, b, c, d, e, f, g, h))
