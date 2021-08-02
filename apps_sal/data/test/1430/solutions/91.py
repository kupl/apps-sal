N, K = map(int, input().split())
S = input()
A, B = [], []
cnt_0, cnt_1 = 0, 0
for i in range(N):
    if S[i] == '0':
        cnt_0 += 1
        if cnt_1 > 0:
            A.append(cnt_1)
        cnt_1 = 0
    else:
        cnt_1 += 1
        if cnt_0 > 0:
            A.append(-cnt_0)
        cnt_0 = 0

if cnt_1 > 0:
    A.append(cnt_1)
if cnt_0 > 0:
    A.append(-cnt_0)

M = len(A)
minus_cnt = 0
s = 0
right = M
for i in range(M):
    if A[i] < 0 and minus_cnt == K:
        right = i
        break
    if A[i] < 0:
        minus_cnt += 1
    s += abs(A[i])

left = 0
ans = s
while right < M:
    for i in range(2):
        if not right < M: break
        s += abs(A[right])
        right += 1

    while left < M:
        if A[left] < 0:
            s -= abs(A[left])
            left += 1
            break
        s -= abs(A[left])
        left += 1

    ans = max(ans, s)

print(ans)
