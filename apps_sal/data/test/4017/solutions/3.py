n = int(input())

a = list(map(int, input().split()))

sort_a = sorted(a)

max_fi = sort_a[-1]
max_se = sort_a[-2]

sum_a = sum(a)
ans = 0
ans_a = []
for i in range(0, n):
    if a[i] != max_fi:
        if sum_a - max_fi - a[i] == max_fi:
            ans += 1
            ans_a.append(i + 1)
    else:
        if sum_a - max_se - a[i] == max_se:
            ans += 1
            ans_a.append(i + 1)

print(ans)
if ans > 0:
    print(' '.join([str(n) for n in ans_a]))
