n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
for i in range(n - 1, -1, -1):
    if k % a[i] == 0:
        print(k // a[i])
        break
