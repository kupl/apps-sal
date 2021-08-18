n = int(input())
s = input()

t = ""
for i in range(n):
    t += s[i]
    while len(t) >= 3 and t[-3:] == "fox":
        t = t[:-3]
print((len(t)))
