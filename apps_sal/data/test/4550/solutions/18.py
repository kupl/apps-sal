S_list = list(map(int, input().split()))
S_max = max(S_list)
answer = sum(S_list) / S_max
if answer == 2:
    result = 'Yes'
else:
    result = 'No'
print(result)
