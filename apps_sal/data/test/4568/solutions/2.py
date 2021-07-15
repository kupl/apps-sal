N = int(input())
S = input()
ans = 0
for i in range(1, N):
    L = set(S[:i])
    R = set(S[i:])
    ans = max(ans, len(L & R))

print(ans)
