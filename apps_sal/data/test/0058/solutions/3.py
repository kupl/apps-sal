n = int(input())
a = int(input())
b = int(input())

sequences = list()
bar_len = (a, b)

for i in range(2 ** 6):
    seq = list()

    for j in range(6):
        seq.append((i & 2 ** j) >> j)

    if sum(seq) == 2:
        sequences.append(seq)


min_count = 10000
for seq in sequences:
    bar = n
    count = 1
    idx = 0

    for i in seq:
        if bar > bar_len[i]:
            bar -= bar_len[i]
        elif bar == bar_len[i]:
            if idx < len(seq) - 1:
                count += 1
            bar = n
        else:
            count += 1
            bar = n - bar_len[i]
        idx += 1
    if count < min_count:
        min_count = count

print(min_count)
