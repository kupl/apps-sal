n = int(input())
s = list(input())
t = []
for i in range(n):
    t.append(s[i])
    if len(t) >= 3 and t[-3] + t[-2] + t[-1] == "fox":
        t.pop(-1)
        t.pop(-1)
        t.pop(-1)
print(len(t))
