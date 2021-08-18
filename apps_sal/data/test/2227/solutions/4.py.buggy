s = input()
s = s.replace("heavy", "1")
s = s.replace("metal", "0")
tmp = ""
for i in s:
    if(i == "1"):
        tmp += "1"
    if(i == "0"):
        tmp += "0"
if len(tmp) == 0:
    print(0)
    return
d = [0 for i in range(10**6 + 1)]
if tmp[len(tmp) - 1] == "0":
    d[len(tmp) - 1] = 1
for i in reversed(list(range(len(tmp) - 1))):
    if tmp[i] == "0":
        d[i] = d[i + 1] + 1
    else:
        d[i] = d[i + 1]
res = 0
for i in range(len(tmp)):
    if tmp[i] == "1":
        res += d[i]
print(res)
