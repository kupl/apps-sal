t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]
    z = arr.count(0)
    su = sum(arr) + z
    if su == 0:
        z += 1
    print(z)
