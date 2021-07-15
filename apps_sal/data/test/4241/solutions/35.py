s = input()

t = input()

ans = []

for i in range(len(s) - len(t) + 1):
    l = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            l += 1

    ans.append(l)

print((min(ans)))

