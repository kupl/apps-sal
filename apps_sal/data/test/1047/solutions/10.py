n = input()
answer = []
for j in range(int(n[0])):
    answer.append(10 ** (len(n) - 1))
for i in range(1, len(n)):
    j = 0
    while j < len(answer) and j < int(n[i]):
        answer[j] += 10 ** (len(n) - i - 1)
        j += 1
    if j < int(n[i]):
        while j < int(n[i]):
            answer.append(10 ** (len(n) - i - 1))
            j += 1
print(len(answer))
print(*answer)
