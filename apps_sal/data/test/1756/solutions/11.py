n, x = list(map(int, input().split()))
d = list(map(int, input().split()))
accum = (3 * n) * [0]
accum2 = (3 * n) * [0]
for i in range(3 * n):
    if i > 0:
        accum[i] = accum[i - 1]
        accum2[i] = accum2[i - 1]
    accum[i] += (((d[i % n] + 1) * d[i % n]) // 2)
    accum2[i] += d[i % n]

ans = 0
temp_ans = (d[0] + 1) * d[0] // 2
j = 0
days = d[0]
for i in range(n):
    while days < x:
        j += 1
        days += d[j % n]
        temp_ans += (d[j % n] + 1) * d[j % n] // 2

    dif = days - x
    if dif == 0:
        ans = max(temp_ans, ans)
    else:
        ans = max(temp_ans - (dif + 1) * dif // 2, ans)
    days -= d[i]
    temp_ans -= (d[i] + 1) * d[i] // 2
print(ans)
