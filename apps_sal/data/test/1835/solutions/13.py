n = int(input())
while n:
    n -= 1
    p = int(input())
    zeroes = 0
    ones = 0
    Lo = []
    Le = []
    for i in range(p):
        S = input()
        z = S.count('0')
        zeroes += z
        ones += len(S) - z
        if len(S) % 2:
            Lo.append(len(S))
        else:
            Le.append(len(S))
    Le.sort()
    Lo.sort()
    if zeroes % 2 == 0 and ones % 2 == 0:
        print(p)
    elif zeroes % 2 == 1 and ones % 2 == 1:
        if len(Lo) > 0:
            print(p)
        else:
            print(p - 1)
    else:
        print(p)
