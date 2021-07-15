n = int(input())
num_list = list(map(int, input().split()))

cnt = 0
min = num_list[0]
for i in range(n):
    if num_list[i] <= min:
        min = num_list[i]
        cnt += 1

print(cnt)
