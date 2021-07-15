# your code goes here
r,g,b = map(int,input().split())
print (min(r+g,g+b,b+r,(r+g+b)//3))
