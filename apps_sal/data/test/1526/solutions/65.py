int_list = list(map(int, input().split()))

int_list_min = sorted(int_list)

max_diff = int_list_min[2] - int_list_min[0]
min_diff = int_list_min[2] - int_list_min[1]
ans = 0

if (max_diff + min_diff) % 2 == 1:
    ans += 1
    min_diff += 1

ans += (max_diff - min_diff) // 2 + min_diff
print(ans)
