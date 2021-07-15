x,y,a,b = map(int,input().split(" "))


result = ( a-x+1 ) * ( (b-y)//2 + 1 ) - ( (a-x)//2 )

print(result)
