mp = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
(a, b) = map(int, input().split())
s = int(0)
for t in range(a, b + 1):
    while t != 0:
        s += mp[t % 10]
        t //= 10
print(s)
