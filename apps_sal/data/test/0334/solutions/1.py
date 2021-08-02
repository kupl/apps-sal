import sys

a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))

cur1, cur2 = b, d
x = set()
y = set()

for i in range(100000):
    x.add(cur1)
    y.add(cur2)
    cur1 += a
    cur2 += c

for i in range(100000):
    if i in x and i in y:
        print(i)
        return

print(-1)
