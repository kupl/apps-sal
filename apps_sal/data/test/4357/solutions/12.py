(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
ls = [a, b, c]
ls.sort()
print(ls[2] * 10 + ls[1] + ls[0])
