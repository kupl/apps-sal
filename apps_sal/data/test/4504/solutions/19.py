S = list(str(input()))
del S[-1]
del S[-1]

def ss(string):
    if len(string)&2==1:
        retrun(False)
    else:
        for i in range(len(string)//2):
            if S[i]!=S[len(string)//2+i]:
                return(False)
        return(True)

while True:
    if ss(S):
        print((len(S)))
        return
    else:
        del S[-1]
        del S[-1]

