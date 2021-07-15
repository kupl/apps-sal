
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(sum((x + y)**2 for x, y in zip(a[:n//2], a[:(n//2)-1:-1])))

