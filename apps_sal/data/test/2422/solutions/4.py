for _ in range (int(input())):
    n=int(input())
    three=n//3
    five=0
    seven=0
    excess=n%3
    if excess==2:
        three-=1
        five=1
    elif excess==1:
        three-=2
        seven+=1
    if three<0:
        print(-1)
    else:
        print(three,five,seven)
