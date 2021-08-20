from math import ceil
(n, k) = map(int, input().split(' '))
cover = 2 * k + 1
turns = ceil(n / cover)
print(turns)
shift = turns * cover - n
first_index = k - shift
if first_index >= 0:
    for i in range(turns):
        print(first_index + 1 + i * cover, end=' ')
else:
    for i in range(turns):
        print(0 + 1 + i * cover, end=' ')
