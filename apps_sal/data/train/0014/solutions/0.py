for _ in range(int(input())):
    (a1, b1) = list(map(int, input().split()))
    (a2, b2) = list(map(int, input().split()))
    if a1 > b1:
        (a1, b1) = (b1, a1)
    if a2 > b2:
        (a2, b2) = (b2, a2)
    flag = False
    if a1 == a2 and a1 == b1 + b2:
        flag = True
    if b1 == b2 and b1 == a1 + a2:
        flag = True
    print('Yes' if flag else 'No')
