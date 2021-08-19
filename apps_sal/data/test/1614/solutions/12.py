(n, h) = [int(x) for x in input().split(' ')]
ai = [int(x) for x in input().split(' ')]
c = 0
for i in range(n):
    if ai[i] > h:
        c += 2
    else:
        c += 1
print(c)
