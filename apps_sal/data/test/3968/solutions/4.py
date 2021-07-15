N = int(input())
A = [int(a) for a in input().split()]

n1 = A.count(1)
n2 = A.count(2)

if n1*n2==0:
    print(*A)
else:
    s1 = (n1-1)//2*2
    ANS = [2,1]+[1]*s1+[2]*(n2-1)+[1]*(n1-1-s1)
    print(*ANS)

