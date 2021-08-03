
n = int(input())
k = int(input())
a = int(input())
b = int(input())
x = n
c = 0

if k == 1:
    print(a * (n - 1))
elif k > x:
    print(a * (x - 1))
else:
    while x >= k:
        if x % k == 0:
            temp = x / k
            if b < (x - (temp)) * a:
                c += b
                x = temp
            else:
                c += a * (x - (temp))
                x = temp
        else:
            t = x % k
            c += (a * t)
            x = x - t
    if x == 1:
        print(int(c))
    else:
        print(int(c) + int((x - 1) * a))
