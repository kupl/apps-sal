N = input()
S = 0
for i in N:
    S += int(i)
if S == 0:
    print('Yes')
elif S < 9:
    print('No')
elif S % 9 == 0:
    print('Yes')
else:
    print('No')

