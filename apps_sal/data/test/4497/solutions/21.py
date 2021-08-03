def cnt_div_two(n):
    res = 0
    while n % 2 == 0:
        n //= 2
        res += 1
    return res


ans = 0
max_cnt = -1
for i in range(1, int(input()) + 1):
    cdt = cnt_div_two(i)
    if cdt > max_cnt:
        ans = i
        max_cnt = cdt
print(ans)
