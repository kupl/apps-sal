n = int(input())
r = n * 2 - 1
h = 0
for i in range(n):
    t = int(input())
    r += abs(h - t)
    h = t
print(r)
