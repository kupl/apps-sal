N = int(input())
S = input()
pre = S[0]
ans = 1
for s in S:
    if pre != s:
        ans += 1
    pre = s
print(ans)
