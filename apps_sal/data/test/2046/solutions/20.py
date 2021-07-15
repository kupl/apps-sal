n = int( input() )
L =  list( map(int,input().split())  )

exp = n ; 
T = [-1]*(n + 1)  ;

miss = 0
for i in range( len(L) ):
    T[ L[i] ] = i ;
    
ot = []    
for i in range(len(L)):
    if(L[i] == exp ):
       ot.append(exp)
       exp -= 1 
       while exp > 0 and T[exp] < i and T[exp] > -1 :
           ot.append(exp)
           exp -= 1
       print(*ot)
       ot = []
    else:
        print()

