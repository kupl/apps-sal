__author__ = 'Utena'
(a, b) = map(int, input().split())
n = 2
t = 0
n1 = 1
c = 0
while True:
    if n1 > b:
        break
    else:
        n *= 2
        n1 = n - 1
        c += 1
        n2 = 1
        for i in range(c):
            if n1 - n2 >= a and n1 - n2 <= b:
                t += 1
            n2 *= 2
print(t)
