N = int(input())
S_list = [int(input()) for i in range(N)]
p_max = max(S_list)
p_sum = sum(S_list)
result = int(p_max / 2) + p_sum - p_max
print(result)
