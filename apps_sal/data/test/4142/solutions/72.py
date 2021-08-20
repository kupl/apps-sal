S = input()
answer = 'Yes'
for i in range(len(S)):
    j = i + 1
    if j % 2 == 0:
        if 'R' in S[i]:
            answer = 'No'
    elif 'L' in S[i]:
        answer = 'No'
print(answer)
