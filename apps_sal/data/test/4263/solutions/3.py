s = input()
score = 0
ans = []
for i in s:
    if i in {'A', 'T', 'C', 'G'}:
        score += 1
    else:
        score = 0
    ans.append(score)
print(max(ans))
