s_ = input()
t_ = input()
s = [c for c in s_]
t = [c for c in t_]
n = len(s)
m = len(t)
for i in reversed(list(range(m - 1, n))):
    replaced = 0
    if s[i] == t[-1] or s[i] == "?":
        k = i - 1
        """
        if k+1<m-1:
            continue
        """
        replace = 1
        for j in reversed(list(range(m - 1))):
            if s[k] == t[j] or s[k] == "?":
                if j == 0:
                    replace = 1
                    break
            else:
                replace = 0
                break
            k -= 1

        if replace:
            k = i
            for j in reversed(list(range(m))):
                s[k] = t[j]
                k -= 1
            replaced = 1
    if replaced:
        break
if n < m:
    replaced = 0
if replaced:
    for i in range(n):
        if s[i] == "?":
            s[i] = "a"
    print(("".join(s)))
else:
    print("UNRESTORABLE")
