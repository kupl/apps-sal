S = input()

if len(S) >= 1 and len(S) <= 1000 and str.islower(S):
    if S[-1] != 's':
        print(S + 's')
    else:
        print(S + 'es')
