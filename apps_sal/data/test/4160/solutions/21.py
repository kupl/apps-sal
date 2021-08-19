x = int(input())
res = 0
m = 100
while m < x:
    m *= 101
    m //= 100
    res += 1
print(res)
