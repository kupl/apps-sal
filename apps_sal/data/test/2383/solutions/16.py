n = int(input())
num_list = list(map(int, input().split()))
min = num_list[0]
for j in range(1, n, 1):
    if num_list[j] < min:
        min = num_list[j]
if min != 1:
    ans = -1
else:
    target = 1
    cnt = 0
    for i in range(len(num_list)):
        if num_list[i] == target:
            target += 1
        else:
            cnt += 1
    ans = cnt
print(ans)
