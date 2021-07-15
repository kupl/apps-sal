import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

    
if n % 2 == 0:
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    print(" ".join(map(str, a)))

else:
    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1
    min_a = 10**10
    for i in range(n):
        if a[i] < min_a:
            min_a = a[i]
            min_ind = i
    a[min_ind] = -a[min_ind] - 1
    print(" ".join(map(str, a)))


