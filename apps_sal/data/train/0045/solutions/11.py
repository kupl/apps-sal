from bisect import bisect_right
t = int(input())
a = []
s = 0
x = 2
while s <= 10 ** 18:
    s += x * (x - 1) // 2
    a.append(s)
    x *= 2
for _ in range(t):
    print(bisect_right(a, int(input())))
