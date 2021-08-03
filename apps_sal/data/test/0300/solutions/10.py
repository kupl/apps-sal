n = int(input())
r = 4.5 * n
t = sorted([int(i) for i in input().split()])

c = 0
s = sum(t)
while(s < r):
    s += 5 - t[c]
    c += 1

print(c)
