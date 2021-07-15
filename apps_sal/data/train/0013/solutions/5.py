t = int(input())
for q in range(t):
    n, g, b = [int(i) for i in input().split()]
    num = n
    n = n // 2 + n % 2
    val = n // g
    d = 0
    if n % g == 0:
        d = (val - 1) * (b + g) + g
    else:
        d = val * (b + g) + n % g
    if d < num:
        print(num)
    else:
        print(d)
    

