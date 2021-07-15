a,b = map(int,input().split())

mylist = [a + b, a - b, a * b]

newlist = sorted(mylist,reverse = True)

print(newlist[0])
