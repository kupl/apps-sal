testCases = int(input())
answers = []
for i in range(testCases):
    a = input().split()
    answers.append(a)
count = 0
for i in range(testCases):
    flag = 0
    ans = answers[i].count('T')
    for j in range(testCases):
        if answers[i][j] == 'T' and i != j:
            if answers[i] == answers[j]:
                continue
            else:
                flag = 1
                break
    if flag == 0 and count < ans:
        count = ans
print(count)
