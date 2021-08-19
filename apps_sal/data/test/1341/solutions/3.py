import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
s = my_file.readline()
t = my_file.readline()
res = 1
for char in t:
    if char == s[0]:
        res += 1
        s = s[1:]
print(res)
