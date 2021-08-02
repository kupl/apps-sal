from collections import Counter

input()
lengths = [int(i) for i in input().split()]
cnt = Counter(lengths)
lengths.sort(reverse=True)
total_square = 0

for le in lengths:
    if cnt[le] % 2 != 0:
        if cnt[le - 1] > 0:
            cnt[le - 1] += 1
        cnt[le] -= 1

for le in lengths:
    if cnt[le] >= 4:
        cnt[le] -= 4
        total_square += le ** 2
    elif cnt[le] < 4 and cnt[le] > 0:
        min_le = le - 1
        while min_le > 0 and cnt[min_le] < 2:
            min_le -= 1
        cnt[le] -= 2
        cnt[min_le] -= 2
        total_square += le * min_le

print(total_square)
