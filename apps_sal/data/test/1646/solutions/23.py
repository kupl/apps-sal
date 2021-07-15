input()
s=input()
if len(s) == 1 and s.count('0')==1:
    print(0)
else:
    k=s.count('0')
    print('1'+k*'0')


