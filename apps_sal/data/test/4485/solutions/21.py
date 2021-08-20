(n, m) = map(int, input().split())
arr = []
for i in range(m):
    (a, b) = map(int, input().split())
    arr.append((a, b))
one = set([b for (a, b) in arr if a == 1])
last = set([a for (a, b) in arr if b == n])
connect = one & last
if len(connect) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
