N = int(input())
S = input()
ls = [0 for _ in range(N)]
for i in range(N):
    if S[i] == 'W':
        ls[i] = 1
ans = 0
i = 0
j = N - 1
while True:
    if ls[i] == 1 and ls[j] == 0:
        ls[i] = 0
        ls[j] = 1
        i += 1
        j -= 1
        ans += 1
    elif ls[i] == 0 and ls[j] == 0:
        i += 1
    elif ls[i] == 1 and ls[j] == 1:
        j -= 1
    else:
        i += 1
        j -= 1
    if i >= j:
        break
print(ans)
