n = int(input())

best = 360

tab = list(map(int, input().split()))

pre_sum = [0]

for i in range(1, len(tab) + 1):
    pre_sum += [tab[i - 1] + pre_sum[-1]]

for i in range(n + 1):
    for j in range(i, n + 1):
        best = min([best, 2 * abs(180 - (pre_sum[j] - pre_sum[i - 1]))])

print(best);

