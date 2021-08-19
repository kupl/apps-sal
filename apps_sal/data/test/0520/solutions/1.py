n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    print(a[0])
if n == 3:
    print(a[1])
if n == 5:
    print(a[2])
