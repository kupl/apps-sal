S_list = [input() for i in range(2)]
N = list(map(int, S_list[0].split()))
L_list = list(map(int, S_list[1].split()))
L_max = max(L_list)
L_sum = sum(L_list) - L_max
if L_sum - L_max > 0:
    result = 'Yes'
else:
    result = 'No'
print(result)
