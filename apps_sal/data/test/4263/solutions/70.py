import re
S = input()
r = re.findall('[ACTG]+', S)
print(max([len(_) for _ in r], default=0))
