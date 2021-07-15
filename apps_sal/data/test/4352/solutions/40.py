a,b=map(int,input().split())
li=[2,3,4,5,6,7,8,9,10,11,12,13,1]
if li.index(a)<li.index(b):
    print("Bob")
elif li.index(a)>li.index(b):
    print("Alice")
else:
    print("Draw")
