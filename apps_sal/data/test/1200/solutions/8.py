def gcd(a, b):
    while a != 0 and b != 0:
        if b > a:
            b = b % a
        else:
            a = a % b
    if a == 0:
        return b
    else:
        return a


n = int(input())
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])
a = sorted(a)
b = a[1] - a[0]
for i in range(0, len(a) - 1):
    b = gcd(b, a[i + 1] - a[i])
cnt = (a[len(a) - 1] - a[0]) // b + 1
print(cnt - n)
