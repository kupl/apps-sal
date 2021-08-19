def match(s, t):
    if len(s) != len(t):
        return False
    return all((x == y or x == '.' for (x, y) in zip(s, t)))


input()
pat = input()
a = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']
for n in a:
    if match(pat, n):
        print(n)
        break
