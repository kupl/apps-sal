n = int(input())
s = input()
a = []
t = input()
if sorted(s) != sorted(t):
    print(-1)
else:
    for i in range(len(t)):
        j = i
        if s[j] == t[i]:
            continue
        while s[j] != t[i]:
            j += 1
        for x in range(j - 1, i - 1, -1):
            a.append(x + 1)
        s = s[:i] + s[j] + s[i:j] + s[j + 1:]
    print(len(a))
    for i in a:
        print(i, end=' ')
