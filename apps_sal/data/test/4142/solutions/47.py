S = input()
answer = 'Yes'
for i in range(len(S)):
    if i % 2 == 0:
        if 'L' in S[i]:
            answer = 'No'
    elif 'R' in S[i]:
        answer = 'No'
print(answer)
