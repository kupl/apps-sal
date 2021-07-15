a,b=map(int,input().split())

result = max(a+b,a-b)
result = max(result,a*b)
print(result)
