choices = 'Vaporeon, Jolteon, Flareon, Espeon, Umbreon, Leafeon, Glaceon'.split(', ')
choices.append('Sylveon')
choices = list([x.lower() for x in choices])

n = int(input())
s = input()
for can in choices:
    if n != len(can):
        continue
    isValid = True
    for i in range(n):
        if s[i] != '.' and s[i] != can[i]:
            isValid = False
    if isValid:
        print(can)
        break
