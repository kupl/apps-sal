S = input()

if S.startswith('A'):
    if S[1].islower() and S[-1].islower():
        count_lower = 0
        count_C = 0
        for s in S[2:-1]:
            if s == 'C':
                count_C += 1
            if s.islower():
                count_lower += 1
        if count_C == 1 and count_lower == len(S) - 4:
            print('AC')
        else:
            print('WA')
    else:
        print('WA')
else:
    print('WA')
