s = input()[::-1]
t = input()[::-1]
x = ""
for i in range(0, len(s) - len(t) + 1):
    if x == "": x = s[i:i + len(t)]
    else: x = x[1:] + s[i + len(t) - 1]
    flag = True
    for j in range(len(t)):
        if x[j] == "?" or x[j] == t[j]: continue
        else: flag = False
    if flag:
        s = (s[:i] + t + s[i + len(t):])[::-1]
        print(s.replace("?", "a"))
        return
print("UNRESTORABLE")
