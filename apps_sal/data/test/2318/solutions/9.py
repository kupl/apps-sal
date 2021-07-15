n = int(input())
for k in range(n):
    s = input()
    t = input()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            if i < len(s) - 1 and s[i] != s[i + 1]:
                while j < len(t) and s[i] == t[j]:
                    j += 1
                i += 1
            elif i == len(s) - 1:
                while j < len(t) and s[i] == t[j]:
                    j += 1
                i += 1
            else:
                i += 1
                j += 1
        else:
            break
    if i == len(s) and j == len(t):
        print('YES')
    else:
        print('NO')
