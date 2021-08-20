n = int(input())
s = ''
abc = 'abc'
for i in range(n):
    if i < 2:
        s += 'a'
    else:
        for j in abc:
            if s[i - 2] + s[i - 1] + j != j + s[i - 1] + s[i - 2]:
                s += j
                break
print(s)
