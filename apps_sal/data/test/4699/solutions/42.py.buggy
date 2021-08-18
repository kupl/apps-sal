n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(10):
    if i in a:
        b.add(str(i))
while n > 0:
    c = set(list(str(n)))
    if c.isdisjoint(b):
        print(n)
        return
    n += 1
