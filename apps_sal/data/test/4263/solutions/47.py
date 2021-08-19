s = input()
score = 0
ans = 0
for i in s:
    if i in {'A', 'T', 'C', 'G'}:
        score += 1
    else:
        score = 0
    ans = max(score, ans)
print(ans)
