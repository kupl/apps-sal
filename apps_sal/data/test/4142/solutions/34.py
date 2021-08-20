S = str(input())
answer = 'Yes'
for i in range(len(S)):
    j = i + 1
    if j % 2 == 0:
        if S[i] == 'R':
            answer = 'No'
    elif S[i] == 'L':
        answer = 'No'
print(answer)
