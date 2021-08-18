s = "qwertyuiopasdfghjklzxcvbnm"
a = set()
for i in s:
    a.add(i)
n = int(input())
ans = 0
for i in range(n):
    s = input().split()

    if(s[0] == "!" and len(a) == 1):
        ans += 1
    elif len(a) == 1 and s[0] == "?" and i != n - 1:
        ans += 1
    elif s[0] == "?":
        try:
            a.remove(s[1])
        except Exception:
            pass
    elif s[0] == ".":
        for j in s[1]:
            try:
                a.remove(j)
            except Exception:
                pass
    elif s[0] == "!":
        b = dict()
        for j in s[1]:
            b[j] = 1
        for j in a:
            try:
                b[j] += 1
            except Exception:
                pass
        a.clear()
        for j in b:
            if b[j] == 2:
                a.add(j)
print(ans)
