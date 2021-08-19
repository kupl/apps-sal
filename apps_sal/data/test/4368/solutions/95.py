n = input()
n = n.split()
k = int(n[1])
n = int(n[0])
a = 1
b = 0
while a == 1:
    b = b + 1
    if k ** b > n:
        a = 0
print(b)
