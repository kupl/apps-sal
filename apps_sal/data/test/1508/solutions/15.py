n = int(input())
seq = sorted(list(map(int, input().split())))

print(' '.join(map(str, [seq[-1]] + seq[1:-1] + [seq[0]])))
