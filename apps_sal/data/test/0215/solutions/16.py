import re

n = int(input())
s = input()
print(max([len(set(x)) for x in re.split('[A-Z]', s)]))

