(n, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sum((i < x for i in a))
print(x - b + (x in a))
