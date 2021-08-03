import re
input()
An = input().split()
print(min(len((re.findall("0+$", bin(int(a))) + [""])[0]) for a in An))
