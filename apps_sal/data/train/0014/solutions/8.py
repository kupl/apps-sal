for _ in range(int(input())):
    a, b = list(map(int,input().split()))
    c, d = list(map(int,input().split()))
    if b > a:
        a, b = b, a
    if d > c:
        c, d = d, c
    if a == c == b+d:
        print("Yes")
    else:
        print("No")

