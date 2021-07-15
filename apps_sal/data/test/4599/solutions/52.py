n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
x = sum(a[::2])-sum(a[1::2])
print(x)

