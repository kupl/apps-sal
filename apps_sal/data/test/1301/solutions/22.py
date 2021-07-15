import re
sa=int(input())
sa2=input()
names=["jolteon", "flareon", "umbreon", "leafeon", "glaceon", "sylveon"]
if len(sa2)==6:
    print("espeon")
elif len(sa2)==8:
    print("vaporeon")
else:
    for sasa in names:
        if re.match(sa2,sasa,re.I):
            print(sasa)

