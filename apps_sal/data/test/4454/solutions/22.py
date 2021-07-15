from math import ceil

for i in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    x = sum(ar)
    if x % len(ar) == 0:
        print(x // len(ar))
    else:
        print(ceil(x / len(ar)))

