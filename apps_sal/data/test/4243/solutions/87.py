X = int(input())


s = X // 500
a = X % 500
t = a // 5
print((s * 1000 + t * 5))
