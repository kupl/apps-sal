import sys
n,m = list(map(int,input().split(' ')))

answer = 0
if n==1 or m==1 :
    print(n*m)
    return
while n>0 and m>0 :
    if n>m :
        answer+= int(n/m)
        n %=m
    else :
        answer += int(m/n)
        m %=n
print(answer)

