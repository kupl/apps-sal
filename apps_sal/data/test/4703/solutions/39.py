S = str(input())
ans = 0
for i in range(2 ** (len(S) - 1)):
    s = S[0]
    for j in range(len(S) - 1):
        if i >> j & 1:
            s += '+'
        s += S[j + 1]
    ans += eval(s)
print(ans)
