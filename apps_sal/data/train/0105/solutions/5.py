import math
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    b = a[0]
    sumi = 0
    for i in range(1, n):
        c = k - a[i]
        sumi += c // b
    print(sumi)
