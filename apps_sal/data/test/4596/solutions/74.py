n = int(input())
arr = list(map(int, input().split()))

cnt_arr = []

for ele in arr:
    cnt = 0
    while ele % 2 == 0:
        ele /= 2
        cnt += 1
    cnt_arr.append(cnt)
print((min(cnt_arr)))
