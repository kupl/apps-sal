n, x, k = list(map(int, input().split()))
array = list(map(int, input().split()))


def next_x(n):
    return ((n + x - 1) // x) * x


valcount = {}
for a in array:
    valcount[a] = valcount.get(a, 0) + 1

begs = {}
pairs = 0
for val, count in sorted(valcount.items()):
    if k > 0 or val % x != 0:
        beg = next_x(val)
        begs[beg] = begs.get(beg, 0) + count
        from_ = next_x(val - k * x + 1)
        pairs += count * begs.get(from_, 0)
print(pairs)
