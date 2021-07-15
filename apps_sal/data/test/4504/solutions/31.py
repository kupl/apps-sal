S=list(input())


import sys
for i in range(len(S)):
    del S[-1]
    for j in range(len(S)):
        if len(S)%2==0:
            if S[0:len(S)//2]==S[len(S)//2:len(S)]:
                print(len(S))
                return
else:
    print(0)
