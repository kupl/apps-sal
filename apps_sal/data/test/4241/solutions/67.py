s = input()
t = input()
score = 1000
for i in range(len(s) - len(t) + 1):
    tmp = 0
    for j in range(len(t)):
        if s[i + j] != t[j]:
            tmp += 1
    score = min(score, tmp)
print(score)
