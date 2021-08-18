
l = input().split()
n = int(l[0])
x = int(l[1])
curr = 1
tot = 0
for i in range(n):
    p = input().split()
    l = int(p[0])
    r = int(p[1])
    while curr + x <= l:
        curr += x
    tot += r - curr + 1
    curr = r + 1
print(tot)
