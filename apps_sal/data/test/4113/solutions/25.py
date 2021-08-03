N = int(input())

max_4 = 25
max_7 = 14

answer = 'No'
for i in range(max_4 + 1):
    for j in range(max_7 + 1):
        sum = 4 * i + j * 7
        if sum == N:
            answer = 'Yes'
            break
    if answer == 'Yes':
        break

print(answer)
