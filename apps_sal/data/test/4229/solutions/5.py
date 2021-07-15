n = int(input())
a = n //3
a_1 = 3*(a+1)*a//2 
b = n // 5
b_1 = 5*(b+1)*b//2
c = n // 15
c_1 = 15*(c+1)* c//2
print(n*(n+1) // 2 - a_1 - b_1+ c_1)
