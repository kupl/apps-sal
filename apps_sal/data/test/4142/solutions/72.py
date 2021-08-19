S = input()

answer = 'Yes'

for i in range(len(S)):

    j = i + 1
    # print(j)

    if j % 2 == 0:
        if 'R' in S[i]:
            answer = 'No'
    else:
        if 'L' in S[i]:
            answer = 'No'
    # print answer

print(answer)
