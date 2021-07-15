x1,y1=list(map(int,input().split(" ")))
x2,y2=list(map(int,input().split(" ")))

result1=max(x1,x2)-min(x1,x2)
result2=max(y1,y2)-min(y1,y2)

print(max(result1,result2))
