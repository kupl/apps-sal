import copy
n = int(input())
a = [int(x) for x in input().split()]
b = copy.copy(a)
b.sort()
m = (b[n // 2] + b[n // 2 - 1]) // 2
for i in range(n):
    if m < a[i]:
        print(b[n // 2 - 1])
    else:
        print(b[n // 2])
