s = input()

selfs = ['A', 'H', 'I', 'M', 'O', 'o', 'T', 'U', 'V', 'v', 'W', 'w', 'X', 'x', 'Y'] # u and m???

opps = {'b':'d', 'p':'q', 'd':'b', 'q':'p'}

for i in range(int(len(s)/2)+1):
    if s[i] not in selfs:
        if s[i] in opps.keys():
            if opps[s[i]] == s[len(s)-i-1]:
                pass
            else:
                print("NIE")
                return
        else:
            print("NIE")
            return
    else:
        if s[i] != s[len(s)-i-1]:
            print("NIE")
            return

if len(s) % 2 == 1:
    if s[int(len(s)/2)] not in selfs:
        print("NIE")
        return

print("TAK")
