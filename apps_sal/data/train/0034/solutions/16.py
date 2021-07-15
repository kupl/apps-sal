t = int(input())
while t:
    n = int(input())
    o = "1" * (n // 2)
    if n % 2: o = "7" + o[1:]
    print(o)
    t -= 1

