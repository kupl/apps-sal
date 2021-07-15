from re import match

input()
s = input().strip()
for x in ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]:
    if match('^' + s + '$', x):
        print(x)
        return

