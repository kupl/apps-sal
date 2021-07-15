import re
s = input()
smax=0
res = re.search(r"A[A-Z]*Z",s)
print(len(res.group()))
