(a, b) = map(int, input().split())
seq = [x + 1 for x in range(a)]
if a > b + 1:
    seq = seq[:a - b - 1] + seq[:a - b - 2:-1]
else:
    seq = seq[::-1]
print(*seq, sep=' ')
