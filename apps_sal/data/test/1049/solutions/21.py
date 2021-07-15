n, d = list(map(int, input().split()))

max = 0
seq = 0

for i in range(d):
    if '0' in set(input()):
        seq += 1
    else:
        if seq > max:
            max = seq
        seq = 0

if seq > max:
    max = seq

print(max)

