(n, k, q) = map(int, input().split())
count_dict = {s: 0 for s in range(1, n + 1)}
for i in range(q):
    seikaisha = int(input())
    if seikaisha in count_dict:
        count_dict[seikaisha] += 1
    else:
        count_dict[seikaisha] = 0
count_dict_sorted = sorted(count_dict.items(), key=lambda x: x[0])
for (i, j) in count_dict_sorted:
    if k + j - q > 0:
        print('Yes')
    else:
        print('No')
