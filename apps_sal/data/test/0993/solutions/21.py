n, m = list(map(int, input().split()))
alis = list(map(int, input().split()))
my_dict = dict()

tmp = 0

for item in alis:
    tmp += item
    tmp %= m
    if tmp in my_dict:
        my_dict[tmp] += 1
    else:
        my_dict[tmp] = 1

ret = 0

for item in my_dict:
    if item == 0:
        val = my_dict[item]
        ret += val * (val - 1) // 2 + val
    else:
        val = my_dict[item]
        ret += val * (val - 1) // 2

print(ret)
