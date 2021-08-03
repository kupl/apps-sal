s = input()
t: str = input()
n = len(s)
m = len(t)

for i in range(n - m, -1, -1):  # -1からn-m回、１ずつ引いていく
    tlike = s[i: i + m]
    if tlike[0] == t[0] or tlike[0] == "?":
        for j in range(m + 1):
            if j == m:
                print((s[:i] + t + s[i + m:]).replace("?", "a"))
                return
            if tlike[j] == "?":
                continue
            elif tlike[j] != t[j]:
                break

print("UNRESTORABLE")
