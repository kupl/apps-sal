q=int(input())
Query=[list(map(int,input().split())) for i in range(q)]

for n,a,b in Query:
    ANS=n*a
    ANS2=n//2*b+n%2*a

    print(min(ANS,ANS2))

