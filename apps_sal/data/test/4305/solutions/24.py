H,A= map(int, input().split())
x=H
s=0
while H>0:
    H=H-A
    s=s+1

print(str(s))
