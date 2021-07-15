s = list(input())
for i in range(len(s) - 1):
    v = s[i]
    if s[i + 1] == v:
        print((i + 1, i + 2))
        return
    if i + 2 < len(s) and s[i + 2] == v:
        print((i + 1, i + 3))
        return
print((-1, -1))

