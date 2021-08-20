(n, x) = map(int, input().split())
num_list = list(map(int, input().split()))
num_sum = 0
count = 1
for i in range(n):
    num_sum += num_list[i]
    if num_sum > x:
        break
    count += 1
print(count)
