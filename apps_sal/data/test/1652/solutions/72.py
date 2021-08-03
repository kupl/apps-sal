s = input()
s = s[::-1]
hoge = ['maerd', 'remaerd', 'esare', 'resare']
i = 0
j = 0
while i < len(s):
    ans = ''
    while j < len(s):
        ans += s[j]
        if len(ans) > 7:
            print('NO')
            return
        if ans in hoge:
            break
        else:
            j += 1
    j += 1
    i = j
print('YES')
