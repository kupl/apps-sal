t = int(input())
for i in range(t):
    n = int(input())
    s = ''
    if n % 2:
        s = '7'
        n -= 3
    else:
        s = '1'
        n -= 2
    s += '1' * (n // 2)
    print(s)

