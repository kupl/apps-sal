def prefix_func(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        j = p[i - 1]
        while j > 0 and s[i] != s[j]:
            j = p[j - 1]
        if s[i] == s[j]:
            j += 1
        p[i] = j
    return p[-1]


n = int(input())
s = input().split()
ans = [*s[0]]
for i in s[1:]:
    c = [*i] + ['$'] + ans[-min(len(i), len(ans)):]
    j = prefix_func(c)
    for _ in range(j):
        ans.pop()
    ans.extend([*i])
print(''.join(ans))
