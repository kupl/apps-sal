input()
seq = [int(num) for num in input().split()]
nums = reversed(sorted(map(int, input().split())))

ind = 0
for num in nums:
    while seq[ind] > 0:
        ind += 1
    seq[ind] = num

for prev, nxt in zip(seq, seq[1:]):
    if prev >= nxt:
        print('Yes')
        return
print('No')

