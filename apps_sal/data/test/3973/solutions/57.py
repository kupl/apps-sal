from collections import defaultdict


n, m = map(int, input().split())
light_list = list(map(int, input().split()))
ret = 0

diff_dict = defaultdict(int)
cnt=0
for i in range(n-1):
    if light_list[i+1] > light_list[i]:
        diff_dict[light_list[i+1]+1] += light_list[i+1] - light_list[i]
        ret += light_list[i+1] - light_list[i]
    else:
        diff_dict[light_list[i+1]+1] += m - (light_list[i] - light_list[i+1])
        ret += light_list[i+1]
        cnt += 1


ret_min = float('inf')
for i in range(1, m+1):
    if i-1 == light_list[0]:
        cnt += 1
    if i-1 == light_list[-1]:
        cnt -= 1
    if diff_dict[i]:
        ret += diff_dict[i]
    ret -= cnt
    ret_min = min(ret+cnt, ret_min)




print(ret_min)
