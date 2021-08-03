import re

t = int(input())
pat = input()
pat = '^' + pat + '$'
if re.match(pat, "vaporeon", re.M | re.I):
    print("vaporeon")
elif re.match(pat, "jolteon", re.M | re.I):
    print("jolteon")
elif re.match(pat, "flareon", re.M | re.I):
    print("flareon")
elif re.match(pat, "espeon", re.M | re.I):
    print("espeon")
elif re.match(pat, "umbreon", re.M | re.I):
    print("umbreon")
elif re.match(pat, "leafeon", re.M | re.I):
    print("leafeon")
elif re.match(pat, "glaceon", re.M | re.I):
    print("glaceon")
elif re.match(pat, "sylveon", re.M | re.I):
    print("sylveon")
