(n, m, c) = list(map(int, input().split(' ')))
b_arr = list(map(int, input().split(' ')))
ans = 0
a_arr = []
for _ in range(n):
    a_arr = list(map(int, input().split(' ')))
    sum_num = c
    for i in range(m):
        sum_num += a_arr[i] * b_arr[i]
    if sum_num > 0:
        ans += 1
print(ans)
