k = input().split(" ")
a = int(k[0])
b = int(k[1])
res = 0
p=0
while a!=0:
    res += a
    p += a
    a = p//b
    p = p-a*b
print(res)

