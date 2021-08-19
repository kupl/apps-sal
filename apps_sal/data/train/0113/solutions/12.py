for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    a = abs(a - b)
    c = a // 5
    a -= c * 5
    print(c + a // 2 + a % 2)
