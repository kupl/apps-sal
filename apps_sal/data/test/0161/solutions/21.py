import sys
input = sys.stdin.readline

ANSLIST=set([(1<<i)-1 for i in range(30)])

NOW=int(input())
if NOW in ANSLIST:
    print(0)
    return

ANS=[]
while True:
    if NOW in ANSLIST:
        print(len(ANS)*2)
        print(*ANS)
        return

        
    for i in range(NOW.bit_length(),0,-1):
        if NOW & (1<<(i-1))==0:
            ANS.append(i)
            NOW=NOW^((1<<(i))-1)
            break

    #print(i,((1<<(i-1))-1),NOW)

    if NOW in ANSLIST:
        print(len(ANS)*2-1)
        print(*ANS)
        return

    NOW+=1
        
    
    

