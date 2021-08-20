(N, K) = map(int, input().split())
tmp = 1
num_cnt = 0
while K > tmp:
    tmp *= 2
    num_cnt += 1
nums_list = []
for i in range(1, N + 1):
    for j in range(num_cnt + 1):
        if i * 2 ** j >= K:
            nums_list.append((1 / 2) ** j)
            break
print(sum(nums_list) * (1 / N))
