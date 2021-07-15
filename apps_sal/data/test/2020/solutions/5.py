n = int(input())
h = set()
v = set()
for i in range(n):
    a, b = list(map(int, input().split(' ')))
    h.add(a)
    v.add(b)
print(min(len(h), len(v)))

