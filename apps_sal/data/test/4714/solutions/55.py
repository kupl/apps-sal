a, b = list(map(int, input().split()))
res = 0
for i in range(a, b + 1):
    str_i = str(i)
    if str_i[0] == str_i[-1] and str_i[1] == str_i[-2]:
        res += 1

print(res)
