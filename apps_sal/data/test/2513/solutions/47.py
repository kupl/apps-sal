N = int(input())
S = input()
for t in ["SS", "SW", "WS", "WW"]:
    for i in S[1:-1]:
        if t[-1] == "S":
            if i == "o": t += t[-2]
            else: t += "S" if t[-2] == "W" else "W"
        else:
            if i == "x": t += t[-2]
            else: t += "S" if t[-2] == "W" else "W"

        if t[0] == "S":
            if S[0] == "o": f = t[-1] == t[1]
            else: f = t[-1] != t[1]
        else:
            if S[0] == "x": f = t[-1] == t[1]
            else: f = t[-1] != t[1]

        if t[-1] == "S":
            if S[-1] == "o": g = t[-2] == t[0]
            else: g = t[-2] != t[0]
        else:
            if S[-1] == "x": g = t[-2] == t[0]
            else: g = t[-2] != t[0]

    if f and g:
        print(t)
        return

print(-1)
