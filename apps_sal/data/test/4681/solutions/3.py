n = int(input())
num_list = [0] * (n + 1)
num_list[0] = 2
num_list[1] = 1
for i in range(2, n + 1, 1):
    num_list[i] = num_list[i - 1] + num_list[i - 2]
ans = num_list[n]
print(ans)
