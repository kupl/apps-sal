sdvig = input()
s = input()
word = list(s)
Querty = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
if sdvig == 'R':
    for i in range(len(s)):
        word[i] = Querty[Querty.index(s[i]) - 1]
elif sdvig == 'L':
    for i in range(len(s)):
        word[i] = Querty[Querty.index(s[i]) + 1]
print(''.join(word))
