S = input()
N = len(S)

cnt_1 = 0
cnt_2 = 0

for i in range(N):
    if i % 2 == 0:
        if S[i] == "0":
            cnt_1 += 1
    else:
        if S[i] == "1":
            cnt_1 += 1

for j in range(N):
    if j % 2 == 0:
        if S[j] == "1":
            cnt_2 += 1
    else:
        if S[j] == "0":
            cnt_2 += 1

print(min(cnt_1, cnt_2))
