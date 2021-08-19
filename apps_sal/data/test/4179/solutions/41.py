(n, m, c) = list(map(int, input().split()))
base_list = list(map(int, input().split()))
double_lists = []
calc_sum = 0
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    double_lists.append(a)
for i in double_lists:
    for (index, j) in enumerate(i):
        calc_sum += j * base_list[index]
    if calc_sum + c > 0:
        ans += 1
    calc_sum = 0
print(ans)
