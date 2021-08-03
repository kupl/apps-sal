n, mb, ma = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]

a, b = ma, mb
for i in range(n):
    if a + b == 0:
        print(i)
        return
    elif a != ma and b > 0 and l[i] == 1:
        b -= 1
        a += 1
    elif a > 0:
        a -= 1
    else:
        b -= 1
print(n)
