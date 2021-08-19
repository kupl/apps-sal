S = input()
ans = 0
(p, n) = (0, 0)
for i in range(len(S)):
    if S[i] == '+':
        p += 1
        n -= 1
    else:
        n += 1
        p -= 1
    n = max(0, n)
    p = max(0, p)
    ans = max(ans, max(n, p))
print(ans)
