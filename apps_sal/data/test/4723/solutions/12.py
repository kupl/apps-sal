s = input()
t = input()
n, m = len(s), len(t)

for i in range(n - m, -1, -1):
    match = True
    for j in range(m):
        if s[i + j] != '?' and s[i + j] != t[j]:
            match = False
            break
    if match:
        print((s[:i].replace('?', 'a') + t + s[i + m:].replace('?', 'a')))
        return
print("UNRESTORABLE")
