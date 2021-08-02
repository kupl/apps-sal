n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
ans = 1
div = []
for i in range(1, int(S**0.5) + 2):
    if S % i == 0:
        if S // i != i:
            div.append(S // i)
            div.append(i)
        else:
            div.append(i)
div.sort()
L = []
for i in range(len(div)):
    cur = div[i]
    mod = []
    for j in range(n):
        if A[j] % cur != 0:
            mod.append(A[j] % cur)
    if len(mod) == 0:
        ans = max(ans, cur)
    else:
        mod.sort()
        mod_dash = []
        for j in range(len(mod)):
            mod_dash.append(cur - mod[j])
        mod2 = [mod[0]]
        mod3 = [mod_dash[0]]
        for j in range(1, len(mod)):
            t = mod2[j - 1] + mod[j]
            mod2.append(t)
            u = mod3[j - 1] + mod_dash[j]
            mod3.append(u)
        c = 10**10
        for j in range(1, len(mod2)):
            c = min(c, max(mod2[len(mod2) - j - 1], mod3[len(mod3) - 1] - mod3[len(mod3) - j - 1]))
        if c <= k:
            ans = max(ans, cur)
print(ans)
