N = int(input())
A = list(map(int, input().split()))
answers = []

for a in A:
    if a % 2 == 0:
        if a % 3 == 0 or a % 5 == 0:
            answer = 'APPROVED'
            answers.append(answer)
        else:
            answer = 'DENIED'
            answers.append(answer)

if 'DENIED' in answers:
    print('DENIED')
else:
    print('APPROVED')
