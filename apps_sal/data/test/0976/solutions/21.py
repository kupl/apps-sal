(n, x) = list(map(int, input().split()))
ans = 0
a = []
t = 0
for i in range(n):
    (l, r) = list(map(int, input().split()))
    a += [[l, r]]
a.sort()
for elem in a:
    ans += (elem[0] - 1 - t) % x + (elem[1] - elem[0] + 1)
    t = elem[1]
print(ans)
