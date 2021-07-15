s = input()
n = len(s)
gcount = 0
pcount = 0
score = 0
for i in range(n):
    if s[i] == "g":
        if gcount > pcount:
            pcount += 1
            score += 1
        else:
            gcount += 1
    else:
        if gcount > pcount:
            pcount += 1
        else:
            gcount += 1
            score -= 1
print(score)
