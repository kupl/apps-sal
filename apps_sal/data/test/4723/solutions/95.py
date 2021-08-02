S = input()
T = input()


def match(s, t):
    for c, d in zip(s, t):
        if c == "?":
            continue
        elif c == d:
            continue
        else:
            return False
    return True


for i in range(len(S) - len(T), -1, -1):
    s = S[i:i + len(T)]
    if match(s, T):
        print((S[:i] + T + S[i + len(T):]).replace("?", "a"))
        return
print("UNRESTORABLE")
