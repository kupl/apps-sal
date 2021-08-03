S = input()
cnt = 0
for i in range(len(S) // 2):
    cnt += S[i] != S[-i - 1]
print(cnt)
