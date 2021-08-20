n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(0, n):
    print(str(a[i]) + ' ' + str(a[2 * n - 1 - i]))
