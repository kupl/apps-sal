L,R = map(int,input().split())
result = 2018
if R - L >= 2019:
    result = 0
else:
    for i in range(L,R):
        for j in range(L+1,R+1):
            result = min(result,i*j%2019)
print(result)
