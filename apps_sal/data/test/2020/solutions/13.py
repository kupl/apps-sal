a = set()
b = set()
clock = int(input())
for i in range(clock):
    c, d = list(map(int, input().split()))
    a.add(c)
    b.add(d)
print(min(len(a), len(b)))
