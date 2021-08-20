S = input()
N = len(S)
for i in range(N - 1, 0, -1):
    if i % 2 == 1:
        continue
    if S[:i // 2] == S[i // 2:i]:
        ans = i
        break
print(ans)
