a = int(input())
if a == 1:
    (b1, c1) = map(int, input().split())
    print(1)
else:
    (b1, c1) = map(int, input().split())
    ch = 2
    (b2, c2) = map(int, input().split())
    for i in range(a - 2):
        (b3, c3) = map(int, input().split())
        if c2 < b2 - b1:
            ch = ch + 1
        elif c2 < b3 - b2:
            ch = ch + 1
            b2 = b2 + c2
        b1 = b2
        c1 = c2
        b2 = b3
        c2 = c3
    print(ch)
