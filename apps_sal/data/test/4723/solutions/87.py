import math

sd = list(input())
t = list(input())

dic = []

slen = len(sd)
tlen = len(t)
for i in range(slen - tlen + 1):
    for j in range(tlen):
        if not (t[j] == sd[i + j] or sd[i + j] == "?"):
            break
    else:
        s = sd[:i] + t + sd[i + tlen:]
        for k in range(len(s)):
            if s[k] == "?":
                s[k] = "a"
        dic.append("".join(s))

if len(dic) == 0:
    print("UNRESTORABLE")
    return
print(sorted(dic)[0])
