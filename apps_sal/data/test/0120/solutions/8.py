n = int(input())
s = input()
if n % 4 != 0:
    print('===')
else:
    sdict = dict()
    for i in 'ACGT?':
        sdict[i] = 0
    for i in s:
        sdict[i] += 1
    exitflag = False
    for i in 'ACGT':
        if sdict[i] > n / 4:
            print('===')
            exitflag = True
            break
    if not exitflag:
        news = ''
        for i in s:
            if i != '?':
                news += i
            else:
                for j in 'ACGT':
                    if sdict[j] < n / 4:
                        sdict[j] += 1
                        inputewith = j
                        break
                news += j
        print(news)
