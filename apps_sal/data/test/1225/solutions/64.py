h = int(input())
res = 1
c = 1
while h > 1:
    c *= 2
    res += c
    h //= 2
print(res)
