(n, a, b) = (int(i) for i in input().split())
ans = 0
for i in range(1, n + 1):
    str_i = str(i)
    sum_i = 0
    for j in str_i:
        sum_i += int(j)
    if a <= sum_i <= b:
        ans += i
print(ans)
