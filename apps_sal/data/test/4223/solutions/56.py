N = int(input())
S = input()
s = S[0]
ans = 1

for i in range(N-1):
    if S[i+1] != s:
        ans += 1
        s = S[i+1]

print(ans)
