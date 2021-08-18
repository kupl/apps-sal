

S = input()
answer = 999

for i in range(len(S) - 2):
    num = int(S[i] + S[i + 1] + S[i + 2])
    if answer > abs(num - 753):
        answer = abs(num - 753)

print(answer)
