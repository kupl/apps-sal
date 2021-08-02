import math

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prev = True
    num = 0
    for j in range(n):
        if prev and a[j] != j + 1:
            num += 1
            prev = False
        elif a[j] == j + 1:
            prev = True
    if num > 2:
        print(2)
    else:
        print(num)
