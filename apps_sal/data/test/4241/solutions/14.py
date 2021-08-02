s = input()
t = input()
a = len(t)
for i in range(len(s) - len(t) + 1):
    a = min(a, sum([x[0] != x[1] for x in zip(t, s[i:])]))
print(a)
