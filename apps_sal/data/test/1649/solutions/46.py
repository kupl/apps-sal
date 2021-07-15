abcd = list(map(int, input().split()))

for bit in range(1 << 4):
    eat = 0
    rem = 0
    for i in range(4):
        if (bit >> i) & 1:
            eat += abcd[i]
        else:
            rem += abcd[i]

        if eat == rem:
            print('Yes')
            return

print('No')
