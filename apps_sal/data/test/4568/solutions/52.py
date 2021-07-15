N = int(input())
S = input()
ans = 0
for i in range(N):
    s1 = set(S[:i])
    s2 = set(S[i:])
    ans = max(len(s1 & s2), ans)
print(ans)
