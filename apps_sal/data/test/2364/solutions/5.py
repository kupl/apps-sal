n = int(input())
data = list(map(int, input().split()))
answer = 0
prefix_data_sum = 0
prefix_answer_sum = 0
prefix = 0
mod = 998244353
for i in range(n):
    prefix += data[i]
    prefix %= mod
    answer = (prefix + prefix_data_sum + prefix_answer_sum) % mod
    prefix_data_sum *= 2
    prefix_data_sum = (prefix_data_sum + prefix) % mod
    prefix_answer_sum = (prefix_answer_sum + answer) % mod
print(answer)
