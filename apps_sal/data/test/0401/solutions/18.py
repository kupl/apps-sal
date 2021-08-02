n, m = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
c = 0
for i in range(n):
    if b.count(a[i]) != 0:
        print(a[i])
        c = 1
        break
if c == 0:
    k = a[0]
    n = b[0]
    print(str(min(n, k)) + str(max(n, k)))
