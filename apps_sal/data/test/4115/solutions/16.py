S = input()
answer = 0
for i in range(len(S) // 2):
    if S[i] != S[-i - 1]:
        answer += 1
print(answer)
