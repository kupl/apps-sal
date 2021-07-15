S = list(input())
K = int(input())

ref = 0
for i in range(len(S)):
    if S[i] == "1":
        ref += 1
    else:
        break

ans = ""
if ref == 0:
    ans = S[0]
else:
    if ref >= K:
        ans = "1"
    else:
        ans = S[ref]

print(ans)
