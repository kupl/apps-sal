S = list(input())
ans = "yes"
for i in range(len(S)):
    ch = S[i]
    S[i] = "-1"
    if ch in S:
        ans = "no"
        break
print(ans)
