S = input()
T = input()

ans = len(T)

for s in range(len(S)):
    if len(S) - s < len(T):
        break
    count = 0
    for t in range(len(T)):
        if S[s + t] != T[t]:
            count += 1

    ans = min(count, ans)

print(ans)
