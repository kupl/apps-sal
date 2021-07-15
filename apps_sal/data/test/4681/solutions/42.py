n = int(input())
a = 2
b = 1
c = 3
for i in range(n):
    c = b + a
    a = b
    b = c
print(a)
