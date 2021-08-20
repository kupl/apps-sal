n = int(input())
a = [int(x) for x in input().split()]
r = 0
d = set()
for x in a:
    while x in d:
        x += 1
        r += 1
    d.add(x)
print(r)
