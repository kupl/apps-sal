import re

n = int(input())
s = [1 if x == "B" else 0 for x in list(input())]
print(sum([el * 2 ** i for i, el in enumerate(s)]))
