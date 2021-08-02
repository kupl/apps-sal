N = int(input())
S = input()


def f(s, t):
    set_s = set()
    set_t = set()
    for i in s:
        set_s.add(i)
    for i in t:
        set_t.add(i)
    return len(set_s & set_t)


ans = 0
for i in range(1, N):
    s = S[i:]
    t = S[:i]
    ans = max(ans, f(s, t))
print(ans)
