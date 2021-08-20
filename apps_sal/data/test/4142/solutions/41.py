S = str(input())
answer = 'Yes'
for i in range(len(S)):
    j = i + 1
    if i % 2 == 0:
        if S[i] == 'L':
            answer = 'No'
    elif S[i] == 'R':
        answer = 'No'
print(answer)
