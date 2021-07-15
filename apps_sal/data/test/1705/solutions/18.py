n = int(input())
v = [int(x) for x in input().split(' ')][::-1]
a = v.index(0)
b = v.index(1)
print(min(n - a, n - b))
