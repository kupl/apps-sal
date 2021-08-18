S = input()
N = len(S)


K = 0
if (N - 1) % 2 == 0:
    K = N - 1
else:
    K = N


step = [i + 1 if S[i] == "R" else i - 1 for i in range(N)]

ans = [1] * N
while K:
    if K & 1:
        new_ans = [0] * N
        for i in range(len(step)):
            new_ans[step[i]] += ans[i]
        ans = new_ans

    step = [step[step[i]] for i in range(N)]
    K >>= 1

print(*ans)
