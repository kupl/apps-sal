x = int(input())
if x % 4 != 0:
    print("===")
    quit()

ct = x // 4
s = input()
aa = s.count('A') - ct
cc = s.count('C') - ct
gg = s.count('G') - ct
tt = s.count('T') - ct
aa = -aa
cc = -cc
gg = -gg
tt = -tt
if min([aa, cc, gg, tt]) < 0:
    print("===")
    quit()
s = list(s)
for i in range(len(s)):
    if s[i] == '?':
        if aa > 0:
            s[i] = 'A'
            aa -= 1
        elif cc > 0:
            s[i] = 'C'
            cc -= 1
        elif gg > 0:
            s[i] = 'G'
            gg -= 1
        else:
            s[i] = 'T'
            tt -= 1
print(''.join(s))
