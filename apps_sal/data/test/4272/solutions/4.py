N = int(input())
S = str(input())
ans = 0
for i in range(N - 2):
    if S[i:i + 3] == 'ABC':
        ans += 1
print(ans)
