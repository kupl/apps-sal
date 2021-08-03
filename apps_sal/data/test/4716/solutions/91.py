N, K = list(map(int, input().split()))
lengths_list = list(map(int, input().split()))
lengths_list.sort()
lengths_list.reverse()
sum_length = 0
for i in range(K):
    sum_length += lengths_list[i]

print(sum_length)
