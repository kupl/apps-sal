k_num, s_num = map(int, input().split())

cnt = 0
for x in range(k_num+1):
    l = s_num - x
    for y in range(k_num+1):
        z = l - y
        if 0 <= z <= k_num:
            cnt += 1

print(cnt)
