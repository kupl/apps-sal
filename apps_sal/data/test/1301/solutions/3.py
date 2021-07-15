import sys
import re

input()
r = re.compile('^'+input()+'$')
l = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]

for i in l:
    if r.match(i):
        print(i)
        return

