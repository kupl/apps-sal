import re

n = int(input())
regexp = re.compile(input())

for i in ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon', 'sylveon']:
    match = regexp.match(i)
    if match and match.group(0) == i:
        print(i)
