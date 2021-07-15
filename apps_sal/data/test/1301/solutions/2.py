names = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
n = int(input())
s = input()
for name in names:
    flag = len(name) == len(s)
    if flag:
        for i in range(len(s)):
            if s[i] != '.' and s[i] != name[i]:
                flag = False
    if flag:
        print(name)
        break
    

