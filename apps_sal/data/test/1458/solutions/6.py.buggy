n = int(input())
s = input()

g = list(s)
if sorted(g) == g:
    print('NO')
else:
    print('YES')
    b = 'a'
    l = 0
    for i in range(len(s)):
        if s[i] < b:
            print(l, i + 1)
            return
        elif s[i] > b:
            b = s[i]
            l = i + 1
