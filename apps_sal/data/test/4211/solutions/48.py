n = int(input())
num_list = list(map(int, input().split()))
a_list = [0] * n
a_list[0] = num_list[0]
for i in range(1, n, 1):
    if i != n - 1:
        a_list[i] = min(num_list[i - 1], num_list[i])
    else:
        a_list[i] = num_list[-1]
sum = 0
for j in a_list:
    sum += j
print(sum)
