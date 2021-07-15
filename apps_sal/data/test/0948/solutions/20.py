N,M=list(map(int,input().split()))
Seq=[list(input())for I in range(N)]
Ans=0
for I in range(N-1):
    for J in range(M-1):
        Det=['f','a','c','e']
        Used=[]
        if Seq[I][J]in Det:
            Used.append(Seq[I][J])
            if Seq[I+1][J]in Det and not Seq[I+1][J]in Used:
                Used.append(Seq[I+1][J])
                if Seq[I][J+1]in Det and not Seq[I][J+1]in Used:
                    Used.append(Seq[I][J+1])
                    if Seq[I+1][J+1]in Det and not Seq[I+1][J+1]in Used:
                        '''
                        Seq[I][J]='#'
                        Seq[I+1][J]='#'
                        Seq[I+1][J+1]='#'
                        Seq[I][J+1]='#'
                        '''
                        Ans+=1
print(Ans)

