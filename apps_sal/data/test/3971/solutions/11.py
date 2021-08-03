from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

num_counter = Counter(nums)
tab = [0, num_counter[1]]
for a in range(2, 100001):
    tab.append(max(
        tab[-1],
        tab[-2] + num_counter[a] * a
    ))
print(tab[100000])
