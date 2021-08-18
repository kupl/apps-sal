n, ma, mb = map(int, input().split(" "))
info_med = []
for _ in range(n):
    info_med.append(list(map(int, input().split(" "))))
info_med.sort(key=lambda x: x[2])
dp = []
dp.append([(0, 0, [-1])])

for min_c in range(1, n * 100 + 1):
    temp_list = []
    for i, (a, b, c) in enumerate(info_med):
        if min_c - c >= 0:
            for pre_a, pre_b, pre_i in dp[min_c - c]:
                if pre_i[-1] < i:
                    if (a + pre_a) * mb == (b + pre_b) * ma:
                        print(min_c)
                        return
                    temp_list.append((a + pre_a, b + pre_b, pre_i + [i]))
    dp.append(temp_list)
print("-1")
