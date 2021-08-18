n = int(input())
a = list(map(int, input().split()))
a.sort()
if (a[0] == 1):
    a[0] = 0
else:
    a[0] = 2
print(a[0] - 1)
