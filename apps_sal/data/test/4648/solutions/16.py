tt = int(input())
for loop in range(tt):
    n = int(input())
    d2 = 0
    d3 = 0
    while n % 2 == 0:
        d2 += 1
        n //= 2
    while n % 3 == 0:
        d3 += 1
        n //= 3
    if n != 1 or d3 < d2:
        print(-1)
    else:
        print(d3 + d3 - d2)
