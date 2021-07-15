S = input()

if S[0:3] == 'RRR':
    print(3)
elif S[0:2] == 'RR' or S[1:3] == 'RR':
    print(2)
elif S == 'SSS':
    print(0)
else:
    print(1)
