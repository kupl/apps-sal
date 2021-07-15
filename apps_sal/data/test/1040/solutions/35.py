N = int(input())
s = str(input())

t = ""

for i in range(N):
    t = t + s[i]
    if t[-3:] == "fox":
        t = t[:len(t)-3]

print(len(t))
