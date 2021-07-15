n=int(input())
a=list(map(int,input().split()))
f=0
for i in a:
    if(i%2):
        f=1
if(f):
    print("First")
else:
    print("Second")
