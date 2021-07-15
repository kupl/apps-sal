n = int(input())
i = 1
cur = n
x = 1
while cur > 0:
    a = cur % 10
    cur //= 10
    x *= 10
print((a+1)*x//10 - n)
