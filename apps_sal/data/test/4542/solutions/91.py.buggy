S = str(input())
N = len(S)
D = [0, 0]  # B,W
ans = 0
prev = S[0]
for i in range(N):
    if S[i] == "B":
        D[0] += 1
    else:
        D[1] += 1
    if i >= 1:
        if S[i] == prev:
            continue
        else:
            ans += 1
            prev = S[i]
if D[0] == 0:  # すべてW
    print((0))
    return
elif D[1] == 0:
    print((0))
    return
print(ans)
