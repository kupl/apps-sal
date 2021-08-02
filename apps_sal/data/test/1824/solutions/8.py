n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
b.sort()
for i in range(n):
    if i == n - 1:
        print(a[i])
    else:
        if a[i] != b[i]:
            print(a[i])
            break
a = [int(x) for x in input().split()]
a.sort()
for i in range(n - 1):
    if i == n - 2:
        print(b[i])
    else:
        if b[i] != a[i]:
            print(b[i])
            break
