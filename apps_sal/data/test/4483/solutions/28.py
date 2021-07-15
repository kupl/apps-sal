# 087_a
X=int(input())
A=int(input())
B=int(input())

if (1<= (A+B) and X<= 10000) and (1<=A and A<= 1000) and (1<=B and B<= 1000):
    a=X-A
    b=int(a/B)
    print((a-(b*B)))

