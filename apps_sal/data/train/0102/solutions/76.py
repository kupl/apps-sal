k = int(input())
for i in range(k):
    n = input()
    l = len(n)
    a = (l - 1) * 9
    x1 = int('1' * l)
    x = int('1' * l)
    n = int(n)
    while n >= x:
        a += 1
        x += x1
    print(a)
