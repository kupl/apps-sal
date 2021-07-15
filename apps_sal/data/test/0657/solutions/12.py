A, B = list(map(int, input().split()))
x,y,z = list(map(int, input().split()))

A -= x*2
A -= y
B -= y
B -= 3*z

if A>0:
    A = 0
if B>0:
    B = 0
print(abs(A+B))

