s = str(input())
t = str(input())
score = 0
le = len(s)

for i in range(le):
    if s[i] != t[i]:
        score += 1

print(score)
