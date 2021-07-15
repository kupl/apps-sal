S_list = list(map(int,input().split()))
sum_1 = sum(S_list)
S_list_1 = [sum_1 - i for i in S_list] 
print(min(S_list_1))  
