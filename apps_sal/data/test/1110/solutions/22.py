n = int(input())
c = n
r = 1
if n == 1:
    print(n)
else:
    for i in range(n - 1, 1, -1):
        c += i
        c += r * (i - 1)
        r += 1
    print(c + 1)
