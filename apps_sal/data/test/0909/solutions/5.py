




#r = list(map(int, input().split()))

a = int(input())
b = int(input())
c = int(input())
z1 = a+b+c 
x1 = a*b+c 
x2 = a*(b+c) 
v1 = a+b*c 
v2 = (a+b)*c 
q1 = a*b*c 

res = max(z1, x1, x2, v1, v2, q1)

print(res)
