S = input()
T = input()

for i in range(len(S)-len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if S[i + j] != T[j]: tmp += 1
    ans = tmp if i == 0 else min(tmp,ans)

print(ans)

