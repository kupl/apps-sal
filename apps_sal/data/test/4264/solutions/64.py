N = int(input())
cnt = 0
for i in range(1, N + 1):
    S = list(str(i))
    if len(S) % 2 != 0:
        cnt += 1

print(cnt)
