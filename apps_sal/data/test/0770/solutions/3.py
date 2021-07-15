n = input()
lst = list(map(int, input().split()))

seqs = 0
total = 0
prev = 0

for i in lst:
    if prev:
        if i:
            total += 1
        else:
            prev = 0
    else:
        if i:
            prev = 1
            seqs += 1
            total += 1
if total:
    print(seqs + total - 1)
else:
    print(0)

