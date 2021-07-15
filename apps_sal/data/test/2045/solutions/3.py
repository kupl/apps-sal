def partial(s):
    g, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while g and (s[g] != s[i]):
            g = pi[g - 1]
        pi[i] = g = g + (s[g] == s[i])

    return pi[-1]


n = int(input())
s = input().split()
ans = [*s[0]]

for i in s[1:]:
    c = [*i] + ['$'] + ans[-min(len(i), len(ans)):]
    j = partial(c)
    for _ in range(j):
        ans.pop()
    ans.extend([*i])

print(''.join(ans))
