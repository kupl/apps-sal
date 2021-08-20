m = 0
n = int(input())
while n:
    (p, q) = list(map(int, input().split(' ')))
    if q - p >= 2:
        m += 1
    n -= 1
print(m)
