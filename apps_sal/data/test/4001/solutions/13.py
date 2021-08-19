n = int(input())
d = [int(a) for a in input().split()]
d.sort()
big = d[-1]
for x in range(1, big + 1):
    if big % x == 0:
        d.remove(x)
print(big, d[-1])
