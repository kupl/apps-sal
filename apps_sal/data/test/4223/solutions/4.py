N = int(input())
S = str(input())
cnt = 1
for i in range(1, N):
    if S[i] == S[i - 1]:
        pass
    else:
        cnt += 1
print(cnt)
