N = int(input())
a = map(int, input().split())

result_num_list = [0] * (10 ** 5 + 5)
for i in a:
    result_num_list[i-1] += 1
    result_num_list[i] += 1
    result_num_list[i+1] += 1

print(max(result_num_list))
