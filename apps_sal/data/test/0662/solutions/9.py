n=int(input())
prev=0
play=[1,2]
for x in range(n):
    a=int(input())
    if a not in play:
        print('NO')
        break
    play=[x for x in range(1,4) if (x not in play) or (x in play and x==a)]
    #print(play)
else:
    print('YES')
