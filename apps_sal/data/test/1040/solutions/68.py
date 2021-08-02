N = int(input())
s = input()
t = ""
for n in range(N):
    t += s[n]
    while len(t) >= 3 and t[-3:] == "fox":
        t = t[:-3]
print(len(t))
