n, seq = int(input()), list(map(int, input().split()))
a0, an = seq.pop(seq.index(max(seq))), seq.pop(seq.index(min(seq)))
print(' '.join(map(str, [a0] + sorted(seq) + [an])))
