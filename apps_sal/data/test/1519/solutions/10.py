(n, l, a) = map(int, input().strip().split())
currend = 0
currstart = 0
c = 0
for i in range(n):
    (b, d) = map(int, input().strip().split())
    currstart = b
    c = c + (currstart - currend) // a
    currend = b + d
c = c + (l - currend) // a
print(c)
