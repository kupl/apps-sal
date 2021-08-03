n = int(input())
s = input()
ans = []
minscore = 0
score = 0
for i in range(n):
    if s[i] == '(':
        score += 1
    else:
        score -= 1
    minscore = min(minscore, score)
finalscore = score
for i in range(-minscore):
    ans.append('(')
for i in range(n):
    ans.append(s[i])
for i in range(-minscore + finalscore):
    ans.append(')')
print(''.join(ans))
