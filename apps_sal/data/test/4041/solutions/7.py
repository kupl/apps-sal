s = input()
t = input()
n = len(s)
ans = 0
for i in range(n):
    for j in range(i, n):
        st = s[:i] + s[j + 1:]
        (cur, ok) = (0, 0)
        for ch in st:
            if ch == t[cur]:
                cur += 1
            if cur == len(t):
                ok = 1
                break
        if ok == 1:
            ans = max(ans, len(s) - len(st))
print(ans)
