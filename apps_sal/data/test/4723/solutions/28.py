s = input()
t = input()
l = []
for i in range(len(s)-len(t)+1):
    for j in range(i, i+len(t)):
        if s[j] != "?" and s[j] != t[j-i]:
            break
    else:
        l.append(s[:i]+t+s[i+len(t):])
if len(l) == 0:
    print("UNRESTORABLE")
    return
l.sort()
print(l[0].replace("?", "a"))
