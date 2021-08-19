S = input()
T = input()

ans = len(T)

# Sの何文字目から調べるかを全探索
for start in range(0, len(S) - len(T) + 1):
    diff = 0
    for i in range(0, len(T)):
        if T[i] != S[start + i]:
            diff += 1
    if ans > diff:
        ans = diff
print(ans)
