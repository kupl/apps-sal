N, L = map(int, input().split())
aji_list = [L + i - 1 for i in range(1, N + 1)]

basic = abs(sum(aji_list))
min_diff = 9999999
for i in aji_list:
    diff = abs(basic - abs(basic - abs(i)))
    min_diff = min(min_diff, diff)

for i in aji_list:
    if abs(basic - abs(basic - abs(i))) == min_diff:
        if basic == sum(aji_list):
            print(basic - abs(i))
        else:
            print(-1 * (basic - abs(i)))
        break
