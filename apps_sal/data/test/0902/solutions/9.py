(n, k) = map(int, input().split())
a = [int(x) for x in input().split()]
p = a[0]
c = 0
for i in range(1, n):
    if p == n:
        print(p)
        break
    if p > a[i]:
        c += 1
        if c == k:
            print(p)
            break
    else:
        p = a[i]
        c = 1
        if p == n:
            print(p)
            break
