N = int(input())
for c4 in range(26):
    for c7 in range(16):
        c = 4 * c4 + 7 * c7
        if c == N:
            print('Yes')
            return
print('No')
