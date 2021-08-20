n = int(input())
l_list = list(map(int, input().split()))
l_sorted = sorted(l_list, reverse=True)
combination_count = 0
for i in range(n - 2):
    l1 = l_sorted[i]
    for j in range(i + 1, n - 1):
        l2 = l_sorted[j]
        for k in range(j + 1, n):
            l3 = l_sorted[k]
            if len(set([l1, l2, l3])) == 3:
                if l1 < l2 + l3:
                    combination_count += 1
                else:
                    break
print(combination_count)
