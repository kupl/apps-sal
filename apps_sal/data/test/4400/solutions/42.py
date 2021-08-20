S = input()
if S == 'RSR' or S == 'RSS' or S == 'SRS' or (S == 'SSR'):
    print(1)
elif S == 'RRS' or S == 'SRR':
    print(2)
elif S == 'RRR':
    print(3)
else:
    print(0)
