import sys
my_file = sys.stdin
s = my_file.readline()
t = my_file.readline()
res = 1
for char in t:
    if char == s[0]:
        res += 1
        s = s[1:]
print(res)
