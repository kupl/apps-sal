(a, b, k) = map(int, input().split())
num_limit = b - a + 1
if num_limit <= k * 2:
    ans_list = [i for i in range(a, b + 1, 1)]
else:
    ans_list = []
    for j in range(k):
        low = a + j
        high = b - j
        ans_list.append(low)
        ans_list.append(high)
    ans_list.sort()
for l in ans_list:
    print(l)
