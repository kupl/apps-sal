Q = int(input())

for q in range(Q):
    n, k = [int(x) for x in input().split()]
    maximum = (n//k)*k + k//2
    print(min([maximum, n]))
