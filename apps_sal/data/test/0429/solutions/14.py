s = input()
if(len(s) < 26):
    print(-1)
else:
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
    letters = dict()
    x = list(s)
    found = False
    for i in range(0, len(x)-25):
        oneCount = 0
        zeroCount = 0
        qCount = 0
        for j in key:
            letters[j] = 0
        for j in range(i, i+26):
            letters[x[j]] += 1
        for j in letters:
            if(letters[j] == 1) and (j.isalpha()):
                oneCount += 1
            elif(letters[j] == 0) and (j.isalpha()):
                zeroCount += 1
            elif(j == '?'):
                qCount += letters[j]
        if(qCount != zeroCount) or (oneCount + zeroCount != 26):
            continue
        else:
            for k in range(i, i+26):
                if(x[k] == '?'):
                    for j in letters:
                        if(letters[j] == 0) and (j.isalpha()):
                            x[k] = j
                            letters[j] += 1
                            break
            for k in range(len(x)):
                if(x[k] == '?'):
                    x[k] = 'A'
            print(''.join(x))
            found = True
            break
    if(found == False):
        print(-1)
