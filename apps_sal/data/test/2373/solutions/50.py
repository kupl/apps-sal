N = int(input())
P = list(map(int, input().split()))
cnt = 0
i = 0
while i <= N - 1:
    if i == N - 1 and P[i] == i + 1:
        cnt += 1
    elif P[i] == i + 1 and P[i + 1] == i + 2:
        cnt += 1
        i += 1
    elif P[i] == i + 1:
        cnt += 1
    i += 1
print(cnt)
