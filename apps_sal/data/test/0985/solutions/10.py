n = int(input())

l, r = [0] * 1999, [0] * 1999

count = 0
for _ in range(n):
    x, y = [int(x) for x in input().split()]
    ldiag = (x + y) - 2
    rdiag = (x + (1001 - y)) - 2
    count += l[ldiag] + r[rdiag]
    l[ldiag] += 1
    r[rdiag] += 1

print(count)
