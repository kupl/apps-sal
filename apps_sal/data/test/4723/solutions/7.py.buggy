S = list(input())
T = list(input())
s = len(S)
t = len(T)
for i in range(s - t, -1, -1):
    ss = S[i:i + t]
    for j in range(t):
        if ss[j] != "?" and ss[j] != T[j]:
            break
    else:
        for j in range(t):
            if ss[j] == "?":
                S[i + j] = T[j]
        break
else:
    print("UNRESTORABLE")
    return
for i in range(s):
    if S[i] == "?":
        S[i] = "a"
print("".join(S))
