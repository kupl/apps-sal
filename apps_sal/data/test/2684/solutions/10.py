def palin(s):
    if s == s[::-1]:
        return 'YES'
    else:
        return 'NO'


try:
    N = int(input())
    S = input()
    es = [S[i: j] for i in range(len(S)) for j in range(i + 1, len(S) + 1)]
    length = 1
    b = S[0]
    for i in es:
        a = palin(i)
        if a == 'YES':
            if len(i) > length:
                length = len(i)
                b = i
        else:
            pass
    print(length)
    print(b)
except:
    pass
