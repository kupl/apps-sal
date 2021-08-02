a, b, k = map(int, input().split())
small = [i for i in range(a, a + k) if a <= i <= b]
big = [i for i in range(b - k + 1, b + 1) if a <= i <= b]
for i in range(len(small)):
    if small[i] not in big:
        big.append(small[i])
big.sort()
for i in range(len(big)):
    print(big[i])
