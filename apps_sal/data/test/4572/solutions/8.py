import string

s = list(map(str, input()))
s = list(set(s))
s.sort()

ans = ""
arr = []

alp = list(map(str, string.ascii_lowercase))
for char in s:
    alp.remove(char)

if len(alp) == 0:
    print("None")
else:
    print((alp[0]))
