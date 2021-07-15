for _ in range(int(input())):
    n = int(input())
    s = [list(input()) for _ in range(n)]
    for elem in s:
        elem.sort()
    numberZeroes = 0
    numberOnes = 0
    numOdd = 0
    for elem in s:
        if (len(elem) % 2) == 1:
            numOdd += 1
        for num in elem:
            if num == "0":
                numberZeroes += 1
            else:
                numberOnes += 1

    while numOdd > 1:
        if numberOnes > 1:
            numberOnes -= 1
        else:
            numberZeroes -= 1
        numOdd -= 1

    if numOdd == 1:
        if numberOnes % 2 == 1:
            numberOnes -= 1
        elif numberZeroes % 2 == 1:
            numberZeroes -= 1
        elif numberOnes > 0:
            numberOnes -= 1
        else:
            numberZeroes -= 1

    if numberOnes % 2 == 0 and numberZeroes % 2 == 0:
        print(n)
    else:
        print(n-1)

