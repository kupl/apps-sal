n = int(input())
d = {}
for i in range(n):
    a = tuple(map(int, input().split()))
    d[a] = d.get(a, 0) + 1
print(max(d.values()))
