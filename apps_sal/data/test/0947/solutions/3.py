from math import ceil
for _ in range(int(input())):
    n = int(input())
    d = 1
    for i in range(2, ceil(n**(1/2))+1):
        if n % i == 0:
            d = i
            break
    if d == 1:
        print(1, n-1)
    else:
        print(n//d, n-n//d)

