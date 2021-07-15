a,b,c=map(int,input().split())
list=[a,b,c]

list.sort()
if list[0]+list[1]==list[2]:
    print("Yes")
else:
    print("No")
