S = input()
T = input()

l = len(S)
k = len(T)
f = 0


if k > l:
    f = 0
else:
    for i in reversed(list(range(0, l - k + 1))):
        for j in range(k):
            if S[i + j] != T[j] and S[i + j] != "?":
                break
            if j == k - 1:
                f = 1
                s = i
        if f == 1:
            break

if f == 0:
    print("UNRESTORABLE")
else:
    S = S[:s] + T + S[s + k:]
    for i in range(l):
        if S[i] == "?":
            S = S[:i] + "a" + S[i + 1:]
    print(S)
