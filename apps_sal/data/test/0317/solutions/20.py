import string
input()
p = input()
print(["NO", "YES"][all(l in p.lower() for l in string.ascii_lowercase)])
