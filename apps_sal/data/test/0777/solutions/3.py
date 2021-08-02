# I know it's messy

d = {}
s = input()
for i in range(0, len(s) + 1):
    for a in "abcdefghijklmnopqrstuvwxyz":
        d["%s%s%s" % (s[:i], a, s[i:])] = True

print(len(d))
