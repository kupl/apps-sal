n = int(input())
parts = sorted(list(map(int, input().split())))
length = sum(parts) // n
pairs = []
for i in range(len(parts) // 2):
    pairs.append((parts[i], length - parts[i]))
print('\n'.join([' '.join(map(str, pair)) for pair in pairs]))
