N = int(input())
S = input()
ans = 0
for i in range(N):
    l = S[:i]
    r = S[i:]
    now = len(set(l) & set(r))
    ans = max(ans, now)
print(ans)
