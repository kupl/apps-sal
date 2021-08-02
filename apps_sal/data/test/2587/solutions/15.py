t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    e = (n - 1) // 4 + 1
    s = '9' * (n - e) + '8' * e
    print(s)
