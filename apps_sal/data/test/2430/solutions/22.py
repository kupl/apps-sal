n=int(input())
result=n*2-1
h=0
for i in range(n):
    x=int(input())
    result+=abs(h-x)
    h=x
print(result)

