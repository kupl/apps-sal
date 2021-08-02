S = input()

ans = 'Yes'
for i in range(len(S)):

    if i % 2 == 0:
        if 'L' in S[i]:
            ans = 'No'
    else:
        if 'R' in S[i]:
            ans = 'No'

print(ans)
