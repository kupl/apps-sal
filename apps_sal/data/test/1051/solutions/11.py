n = int(input())
a = [int(i) for i in input().split()]
a.sort()
if a[n - 1] <= 25:
    print('0')
else:
    print(a[n - 1] - 25)
