N = int(input())
S = []
M = 1
count = 1

for _ in range(N):
    S.append(input())

S.sort()
ans = [S[0]]

for i in range(N - 1):
    if S[i] == S[i + 1]:
        count += 1
    else:
        if M < count:
            M = count
            ans = [S[i]]
        elif M == count:
            ans.append(S[i])
        count = 1
if M < count:
    M = count
    ans = [S[N - 1]]
elif M == count:
    ans.append(S[N - 1])

ans = list(set(ans))
ans.sort()

for j in range(len(ans)):
    print(ans[j])
