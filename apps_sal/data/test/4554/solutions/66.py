w,a,b = [int(x) for x in input().split()]
a,b = min(a,b) ,max(a,b)

print(max(0,b-a-w))
