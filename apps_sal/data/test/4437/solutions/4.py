n = int(input())
s = input()
a = []
d = 0
for i in range(0, n, 2):
    if s[i] == s[i + 1]:
        a.append('a')
        a.append('b')
        d += 1
    else:
        a.append(s[i])
        a.append(s[i + 1])

print(d)
print("".join(a))
