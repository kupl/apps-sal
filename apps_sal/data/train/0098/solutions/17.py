for _ in range(int(input())):
    (c, m, s) = [int(i) for i in input().split()]
    (a, b) = (min(c, m), max(c, m))
    if s >= a:
        print(a)
    else:
        a = a - s
        b = b - s
        temp = (a + b) // 3
        print(s + min(temp, a))
