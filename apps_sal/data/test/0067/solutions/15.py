from sys import stdin
a,b,c=list(map(int,stdin.readline().strip().split()))
if a>b+c:
    print("+")
elif b>a+c:
    print("-")
elif c==0 and a==b:
    print(0)
else:
    print("?")

