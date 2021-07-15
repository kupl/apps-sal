n,m = list(map(int, input().split()))
answer=0
while True:
    if n >=3 and m>=2:
        
        if n/m>3/2:
            n-=3
            m-=1
        else:
            n-=2
            m-=2
        
            
        answer+=6
    else:
        if m == 1:
            answer += max(3, 2* n)
            break
        elif m == 0:
            answer+= 2*n
            break
        else:
            answer += 3*m
            break
print(answer)

