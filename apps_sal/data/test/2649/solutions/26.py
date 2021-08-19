n = int(input())
maxa = maxb = -2000000000.0
mina = minb = 2000000000.0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    maxa = max(maxa, x + y)
    mina = min(mina, x + y)
    maxb = max(maxb, x - y)
    minb = min(minb, x - y)
print(max(maxa - mina, maxb - minb))
