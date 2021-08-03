n = int(input()) - 1
a = int(input())
b = int(input())
c = int(input())
if n == 0:
    print(0)
else:
    minimum = min(a, b, c)
    print((n - 1) * minimum + min(a, b))
