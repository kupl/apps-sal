(n, p, k) = map(int, input().split())
(p1, p2) = (max(1, p - k), min(n, p + k))
if p1 > 1:
    print('<< ', end='')
for i in range(p1, p2 + 1):
    print(i if i != p else '(' + str(p) + ')', end=' ')
print('>>' if p2 < n else '')
