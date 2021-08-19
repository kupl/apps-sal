L = int(input())
n = L.bit_length()
ans = []
for i in range(1, n):
    ans.append((i, i + 1, 0))
    ans.append((i, i + 1, 2 ** (n - i - 1)))
binL = bin(L)
for i in range(1, n):
    if binL[i + 2] == '1':
        mask = int(binL[:i + 2], 2) << n - i
        ans.append((1, i + 1, L & mask))
print(n, len(ans))
for edge in ans:
    print(*edge)
