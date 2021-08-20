t = int(input())
for _ in range(t):
    (a1, b1) = map(int, input().split())
    (a2, b2) = map(int, input().split())
    if a1 > b1:
        (a1, b1) = (b1, a1)
    if a2 > b2:
        (a2, b2) = (b2, a2)
    if b1 == b2 and a1 + a2 == b1:
        print('Yes')
    else:
        print('No')
