n = int(input())
for i in range(n, n + 111):
    s = str(i)
    if s[0] == s[1] and s[1] == s[2]:
        print(i)
        break
