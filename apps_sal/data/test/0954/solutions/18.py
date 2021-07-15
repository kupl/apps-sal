#CF YL1
s=input()
c={s}
def cyc(s2):return s2[-1]+s2[:-1]
for i in range(len(s)):
    s=cyc(s)
    c.add(s)
print(len(c))

