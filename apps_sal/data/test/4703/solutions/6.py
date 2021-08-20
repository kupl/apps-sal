S = input()
N = len(S)
ans = 0
for i in range(2 ** (N - 1)):
    Bit = list((i + 1 for i in range(N - 1)))
    for j in range(N - 1):
        if i >> j & 1:
            Bit[j] = 0
    Bit = [b for b in Bit if b > 0]
    L = 0
    for b in Bit:
        ans += int(S[L:b])
        L = b
    ans += int(S[L:])
print(ans)
