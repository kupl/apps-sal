S = list(input())

if S[0] == 'A':
    cnt = 0
    for i in range(2, len(S) - 1):
        if S[i] == 'C':
            cnt += 1
    if cnt == 1:
        S.sort()
        for i in range(2, len(S)):
            if S[i].isupper():
                print('WA')
                return
        print('AC')
    else:
        print('WA')
else:
    print('WA')
