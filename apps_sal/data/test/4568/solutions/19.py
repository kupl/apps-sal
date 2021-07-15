n = int(input())
s = input()
a = []
for i in range(1, len(s)):
    s1 = list(s[:i])
    s2 = list(s[i:])
    b = []
    for j in s1:
        if j in s2 and j not in b:
            b.append(j)
    a.append(len(b))
print(max(a))
