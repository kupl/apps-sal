S = input()
count = 0
if S == 'RRR':
    print(3)
elif S == 'SSS':
    print(0)
elif S == 'RRS' or S == 'SRR':
    print(2)
else:
    print(1)
