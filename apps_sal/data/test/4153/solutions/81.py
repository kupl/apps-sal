import math
from collections import Counter
s = list(input())
s = list(map(int, s))
dict_s = Counter(s)
#print(dict_s)
print((min(dict_s[0], dict_s[1]))*2)
