S_list = list(map(int,input().split()))

if  S_list[1] - S_list[0] >= 0 and S_list[2]- S_list[0] >=0 and S_list[1] - S_list[2] >=0:
    result = "Yes"
else:
    result = "No"
print(result)

