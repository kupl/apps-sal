n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
n1 = a[0]
n2 = b[0]
n3 = c[0]
n -= a[0] + b[0] + c[0]
n1 += min(a[1] - a[0], n)
n -= min(a[1] - a[0], n)
n2 += min(b[1] - b[0], n)
n -= min(b[1] - b[0], n)
n3 += n
print(n1, n2, n3)
