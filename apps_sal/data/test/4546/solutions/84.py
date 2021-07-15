S_list = list(map(int,input().split()))
 
if  S_list[1] - S_list[0] == S_list[2] - S_list[1]:
    result = "YES"
else:
    result = "NO"
print(result)
