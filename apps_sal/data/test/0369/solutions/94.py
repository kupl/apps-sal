(N, M) = list(map(int, input().split()))
S = input()
S = S[::-1]
count = 0
count_1 = 0
count_2 = 0
answer = []
ans = 0
for (i, s) in enumerate(S):
    if i == 0:
        pass
    elif i == N:
        count_1 += 1
        answer.append(count_1)
    elif s == '0' and count_1 < M - 1:
        count_1 += 1
        count = count_1
        count_2 = 0
    elif s == '0' and count_1 == M - 1:
        count_1 += 1
        count_2 = 0
        answer.append(count_1)
        count = 0
        count_1 = count
    elif count_1 < M - 1 and count_2 < M - 1:
        count_1 += 1
        count_2 += 1
    elif count_2 == M - 1:
        ans = -1
        break
    elif count_1 == M - 1:
        count_2 += 1
        answer.append(count)
        count_1 = count_2
        count = count_1
if ans == -1:
    print(-1)
else:
    print(' '.join(map(str, answer[::-1])))
