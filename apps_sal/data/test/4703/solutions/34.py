S = input()

n = len(S)

ans = 0
for i in range(2**(n - 1)):
    tmp = 0
    t = 0
    for j in range(n - 1):
        if (i >> j) & 1:
            tmp += int(S[t:j + 1])
            t = j + 1
    tmp += int(S[t:])
    ans += tmp
print(ans)
