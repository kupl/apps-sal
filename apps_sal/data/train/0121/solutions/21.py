t = int(input())
while t:
    n = int(input())
    a = input().split()
    for i in range(2 * n):
        a[i] = int(a[i])
    a.sort()
    print(a[n] - a[n - 1])
    t -= 1
