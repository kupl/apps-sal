s = input()
n = len(s)
for i in range(n - 1, 0, -1):
    s = s[0:i]
    n = len(s)
    if n % 2 != 0:
        pass
    else:
        if s[0:i // 2] == s[i // 2:n]:
            print(n)
            return
