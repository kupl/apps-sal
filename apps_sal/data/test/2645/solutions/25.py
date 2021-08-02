s = input()
n = len(s)
charge = 0
score = 0
for i in range(n):
    if s[i] == 'g':
        if charge > 0:
            score += 1
            charge -= 1
        else:
            charge += 1
    else:
        if charge > 0:
            charge -= 1
        else:
            score -= 1
            charge += 1

print(score)
