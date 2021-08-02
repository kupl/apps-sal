
T = int(input())
n = [0] * T
m = [0] * T
a = [0] * T
b = [0] * T

for t in range(T):
    n, k = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    a.sort()
    b.sort()
    for i in range(k):
        if a[i] < b[n - i - 1]:
            a[i] = b[n - i - 1]
        else:
            break
    print(sum(a))
