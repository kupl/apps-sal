N,K = list(map(int, input().split()))
S = input()
a = K-1
b = N-K
if a ==0:
    a = 1000
if b == 0:
    b =1000
pos = K-1
printed = 1
print('PRINT '+str(S[pos]))
if a<=b:
    while pos!=0:
      print('LEFT')
      pos-=1
      print('PRINT '+str(S[pos]))
      printed+=1
    if printed !=N:
        while pos!=K-1:
            print('RIGHT')
            pos+=1
        while pos!=N-1:
            print('RIGHT')
            pos+=1
            print('PRINT '+str(S[pos]))
            printed+=1
elif a>b:
    while pos!=N-1:
        print('RIGHT')
        pos+=1
        print('PRINT '+str(S[pos]))
        printed+=1
    if printed !=N:
        while pos!=K-1:
            print('LEFT')
            pos-=1
        while pos!=0:
          print('LEFT')
          pos-=1
          print('PRINT '+str(S[pos]))
          printed+=1
        

