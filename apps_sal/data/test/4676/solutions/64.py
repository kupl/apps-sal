o = input()
e = input()

n = len(o) + len(e)
s = ['' for _ in range(n)]
for i in range(n):
    j = i // 2
    if i % 2 == 0:
        s[i] = o[j]
    else:
        s[i] = e[j]

print((''.join(s)))

