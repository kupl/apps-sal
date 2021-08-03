s = input() + '   '
d, ans, DD = {}, 0, {"R": 0, "B": 0, "Y": 0, "G": 0}
for i in range(len(s)):
    if s[i] in "RGBY":
        d[i % 4] = s[i]
for i in range(len(s)):
    if s[i] == "!":
        DD[d[i % 4]] += 1
print(DD["R"], DD["B"], DD["Y"], DD["G"])
