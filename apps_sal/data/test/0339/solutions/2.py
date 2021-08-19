x = int(input())
k = int(input())
a = int(input())
b = int(input())
c = 0
while x > 1:
    if x % k > 0:
        if x > k:
            c += a * (x % k)
            x -= x % k
        else:
            c += a * (x % k - 1)
            x = 1
    elif (x - x // k) * a >= b:
        c += b
        x = x // k
    else:
        c += (x - 1) * a
        x = 1
print(c)
