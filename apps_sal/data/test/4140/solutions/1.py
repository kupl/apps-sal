import copy

S = list(input())
S_ = copy.deepcopy(S)
N = len(S)
ans = N
cnt = 0

for i in range(N - 1):
    if S[i] == S[i + 1]:
        cnt += 1
        if S[i + 1] == "0":
            S[i + 1] = "1"
        else:
            S[i + 1] = "0"

print((min(cnt, ans)))
