S = input()
n = len(S)
ans = 0
for bit in range(1 << n - 1):
    tmp = S[0]
    for i in range(n - 1):
        if bit & 1 << i:
            tmp += '+'
        tmp += S[i + 1]
    ans += sum(map(int, tmp.split('+')))
print(ans)
