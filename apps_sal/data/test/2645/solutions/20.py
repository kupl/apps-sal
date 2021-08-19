s = input()
r = 0
p = 0
score = 0
for x in s:
    if x == 'g':
        if p < r:
            p += 1
            score += 1
        else:
            r += 1
    elif p < r:
        p += 1
    else:
        score -= 1
        r += 1
print(score)
