n = int(input())

if n >= 15:
    x = n * 800
    y = ( n // 15 ) * 200
    print(x - y)
else:
    print(n * 800)
