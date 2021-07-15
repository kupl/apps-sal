n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(n):
    print(a[i], a[2 * n - i - 1])
