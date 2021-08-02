S = list(input())
ans = 'Yes'
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 'L':
            ans = 'No'
            break
    if i % 2 == 1:
        if S[i] == 'R':
            ans = 'No'
            break
print(ans)
