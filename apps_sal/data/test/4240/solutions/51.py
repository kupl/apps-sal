S = input()
T = input()

for i in range(len(S)):
    if S == T:
        print('Yes')
        break
    else:
        lstS = list(S)
        s = lstS.pop()
        a = list(s) + lstS
        S = ''.join(a)
        
else:
    print('No')
