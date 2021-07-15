s = input()
t = input()

soln = ""

for i in range(len(s)-len(t)+1):
    sol = True
    for j in range(len(t)):
        if not (s[i+j] == t[j] or s[i+j] == "?"):
            sol = False
            break

    if sol:
        soln = s[:i] + t + s[i+len(t):]

print(soln.replace("?", "a") if soln != "" else "UNRESTORABLE")
