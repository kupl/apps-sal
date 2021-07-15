def zeroTrim(s):
    while s[0] == '0':
        if len(s) == 1:
            break
        s = s[1:]
    return s

N = input()
K = int(input())

def calc(N, K):
    digit = len(N)
    res = 0

    if K == 1:
        if digit > 1:
            res += (digit - 1) * 9
        res += int(N[0])
    elif K == 2:
        if digit <= 1:
            return 0
        if digit > 2:
            res += 9 * 9 * (digit - 1) * (digit - 2) // 2
        for i in range(int(N[0])-1):
            res += calc('9'*(digit-1), 1)
        res += calc(zeroTrim(N[1:]), 1)
    else:
        if digit <= 2:
            return 0
        if digit > 3:
            res += 9 * 9 * 9 * (digit - 1) * (digit - 2) * (digit - 3) // 6
        
        for i in range(int(N[0])-1):
            res += calc('9'*(digit-1), 2)
        res += calc(zeroTrim(N[1:]), 2)
    return res

print(calc(N, K))
