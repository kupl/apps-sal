S = input()
Sa = S.replace("?", "a")
T = input()
nt = len(T)
ans = list()
for i in range(len(S) - nt + 1):
    X = S[i: i + nt]
    for x, t in zip(X, T):
        if x == "?":
            continue
        if x != t:
            break
    else:
        ans.append(Sa[:i] + T + Sa[i + nt:])
ans.sort()
print((ans[0] if ans else "UNRESTORABLE"))

