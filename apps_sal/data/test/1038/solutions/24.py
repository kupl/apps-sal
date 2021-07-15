A,B = map(int,input().split())
a = A%2>0
b = B%2<1
print((A*a)^(((B-b)-(A-1^a))//2%2)^(B*b))
