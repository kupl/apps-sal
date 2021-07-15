q = input().split()
a = int(q[0])
b = int(q[1])
n = int(q[2])
x = int(q[3])
q = pow(a,n-1,1000000007)
x = q*a*x
if a == 1:
    q = n
else:
    q = (q-1)*pow(a-1,1000000005,1000000007)*a + 1
q = q*b+x
print(q%1000000007)
