def B():
    bra = False
    braWord = False
    nIn = 0
    worOut = [0] * 256
    nOut = 0
    n = int(input())
    str = list(input())
    for i in range(n):
        if not bra:
            if str[i] == '_':
                nOut += 1
            elif str[i] == '(':
                nOut += 1
                bra = True
            else:
                worOut[nOut] += 1
        elif str[i] == '_':
            if braWord:
                nIn += 1
                braWord = False
        elif str[i] == ')':
            if braWord:
                nIn += 1
            braWord = False
            bra = False
        else:
            braWord = True
    print(max(worOut), nIn)


B()
