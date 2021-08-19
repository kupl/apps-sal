for _ in range(int(input())):
    (n, s) = list(map(int, input().split()))
    lenN = len(str(n))
    sumDigit = 0
    nCpy = n
    for j in range(lenN):
        sumDigit += nCpy % 10
        nCpy //= 10
    if sumDigit <= s:
        print(0)
    else:
        for j in range(lenN):
            newN = (n // 10 ** (j + 1) + 1) * 10 ** (j + 1)
            nCpy = newN
            sumDigit = 0
            for j in range(lenN):
                sumDigit += nCpy % 10
                nCpy //= 10
            if sumDigit <= s:
                print(newN - n)
                break
