S = input()
T = input()
N = len(S)
M = len(T)
cnt_min = M
for i in range(N - M + 1):
    count = 0
    for j in range(M):
        if S[i + j] != T[j]:
            count += 1
    if count < cnt_min:
        cnt_min = count
print(cnt_min)
