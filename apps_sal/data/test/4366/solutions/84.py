S_list = list(map(int,input().split()))
ans = S_list[0] + S_list[1]
if  ans <24 :
    result = ans
else:
    result = ans - 24
print(result)

