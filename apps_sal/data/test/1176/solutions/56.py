n = int(input())
a = list(map(int, input().strip().split()))

num_odd_minus = 0
res = 0
min_num = abs(a[0])
for num in a:
    if num < 0:
        num_odd_minus += 1
    abs_num = abs(num)
    res += abs_num
    if min_num > abs_num:
        min_num = abs_num

if num_odd_minus % 2 == 1:
    res -= min_num * 2

print(res)
