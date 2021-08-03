S = input()

n = len(S)
ans = [0 for _ in range(n)]

S += "$"

s = 0
for i in range(n):
    if S[i] != S[i + 1]:
        l = i - s + 1
        if S[i] == "R":
            ans[i + 1] += l // 2
            ans[i] += (l + 1) // 2
        else:
            ans[s] += (l + 1) // 2
            ans[s - 1] += l // 2
        s = i + 1

print((" ".join(map(str, ans))))
