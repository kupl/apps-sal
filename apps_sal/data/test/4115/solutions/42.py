S = input()
T = S[::-1]
cnt = 0
for i in range(len(S)//2):
    if S[i] != T[i]:
        cnt += 1
print(cnt)
