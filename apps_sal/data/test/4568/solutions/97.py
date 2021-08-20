N = int(input())
S = input()
ans = 0
for i in range(N - 1):
    L = S[:i + 1]
    R = S[i + 1:]
    c = 0
    for l in set(L):
        if l in R:
            c += 1
    ans = max(ans, c)
print(ans)
