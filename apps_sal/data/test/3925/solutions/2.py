def mni(i, n):
    return i + 1

def check(s, b):
    res = 1
    i = b
    cur = s[i]
    i = (i + 1) % len(s)
    while i != b:
        if cur != s[i]:
            res += 1
            cur = s[i]
            i = (i + 1) % len(s)
        else:
            break
    return res


S = input()
N = len(S)
if S == 1:
    ans = 1
else:
    ans = 0
    for i in range(len(S)):
        if i == 0 or S[i] == S[(i - 1 + N) % N]:
            ans = max(ans, check(S, i))
print(ans)

