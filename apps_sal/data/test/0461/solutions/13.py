n = int(input())
a = int(input())
b = int(input())
c = int(input())

n -= 1
t = 0
if n > 0:
    t += min([a, b])
    n -= 1
t += min([a, b, c]) * n
print(t)
