S = input()
K = int(input())
i = 0
ans = 1
while i < K:
    if S[i] != '1':
        ans = S[i]
        break
    i += 1
print(ans)
