n = int(input())
s = list(input())
ans = ''
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
prev = ''
eo = False
for i in range(0, s.__len__()):
    if s[i] in vowels:
        if s[i] != prev:
            ans += s[i]
            eo = False
        elif not eo:
            if i != s.__len__() - 1:
                if prev == s[i] == 'e' and s[i + 1] == 'e' or prev == s[i] == 'o' and s[i + 1] == 'o':
                    eo = True
                elif prev == s[i] == 'e' and s[i + 1] != 'e' or prev == s[i] == 'o' and s[i + 1] != 'o':
                    eo = True
                    ans += prev
            else:
                if prev == s[i] == 'e' or prev == s[i] == 'o':
                    ans += prev
    else:
        eo = False
        ans += s[i]
    prev = s[i]
print(ans)
