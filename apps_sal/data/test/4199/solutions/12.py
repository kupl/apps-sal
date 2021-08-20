(mem_num, over_height) = map(int, input().split())
members_hgt = list(map(int, input().split()))
cnt = 0
for i in members_hgt:
    if i >= over_height:
        cnt += 1
print(cnt)
