n = int(input())
a = [int(x) for x in input().split()]
a.sort()
n = len(a)
x = sum(a[:n//2])
y = sum(a[n//2:])
print(x ** 2 + y ** 2)
