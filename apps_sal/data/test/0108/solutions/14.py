from string import ascii_lowercase
s = list(input())
symbs = ascii_lowercase

cursymbol = 0
for d in range(len(s)):
    if s[d] <= ascii_lowercase[cursymbol]:
        s[d] = ascii_lowercase[cursymbol]
        if ascii_lowercase[cursymbol] == 'z':
            print(''.join(s))
            return
        cursymbol += 1
print(-1)

