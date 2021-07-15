n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = a[0]
c1 = b[0]
for i in range(1, n):
    c |= a[i]
    c1 |= b[i]
print(c + c1)
