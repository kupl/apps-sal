from sys import stdin, stdout

A,B = list(map(int, stdin.readline().rstrip().split()))

x,y,z = list(map(int, stdin.readline().rstrip().split()))

A-=2*x
A-=y
B-=y
B-=3*z

crystals=0
if A<0:
    crystals+=-A
if B<0:
    crystals+=-B
    
print(crystals)



