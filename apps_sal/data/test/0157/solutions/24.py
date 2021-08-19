a = int(input())
b = int(input())
c = int(input())
res = 0
while a - 1 >= 0 and b - 2 >= 0 and (c - 4 >= 0):
    a -= 1
    b -= 2
    c -= 4
    res += 7
print(res)
