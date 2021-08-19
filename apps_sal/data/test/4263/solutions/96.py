S = list(input())
temp = 0
ans = 0
letter = ['A', 'T', 'C', 'G']
for (i, val) in enumerate(S):
    if val in letter:
        temp += 1
    else:
        if ans < temp:
            ans = temp
        temp = 0
if ans < temp:
    ans = temp
print(ans)
