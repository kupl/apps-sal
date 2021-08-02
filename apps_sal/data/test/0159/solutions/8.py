n = int(input())
a = [int(s) for s in input().split()]


def evklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


s = ''
k = 0
s += str(a[0])
for i in range(1, n):
    if evklid(a[i], a[i - 1]) != 1:
        k += 1
        s += ' 1 ' + str(a[i])
    else:
        s += ' ' + str(a[i])
print(k)
print(s)
