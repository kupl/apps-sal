a = int(input())
b = [int(input()) for i in range(a)]
b.sort()
c = sum(b)
d = 0
if c % 10 != 0:
    print(c)
else:
    for i in range(a):
        if b[i] % 10 != 0:
            c = c - b[i]
            print(c)
            break
    if sum(b) == c:
        print(0)
