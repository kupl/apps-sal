n = int(input())
t = [int(x) for x in input().split()]
count = min(t.count(1), t.count(2), t.count(3))
print(count)
a = b = c = 0
for i in range(count):
    while t[a] != 1:
        a += 1
    while t[b] != 2:
        b += 1
    while t[c] != 3:
        c += 1
    print(a + 1, b + 1, c + 1)
    a += 1
    b += 1
    c += 1

