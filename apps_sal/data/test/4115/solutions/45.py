S = input()
cnt = 0
N = len(S)
for i in range(N // 2):
    if S[i] != S[N - i - 1]:
        cnt += 1
print(cnt)
