n = int(input())
a = [int(i) for i in input().split()]
a.sort()
b = 0
c = 0
setA = set()
for i in range(1, n):
    if a[i] == a[i - 1]:
        c += 1
        if b > 0:
            b -= 1
            n -= 1
    else:
        b += c
        c = 0
        n -= 1
print(n)
