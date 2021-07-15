form = int(input())
hs, ms = input().split(":")
if int(ms) > 59:
    ms = "0" + ms[1]
if form == 24:
    if int(hs) > 23:
        hs = "0" + hs[1]
else:
    if int(hs) > 12:
        if hs[1] == "0":
            hs = "10"
        else:
            hs = "0" + hs[1]
    elif int(hs) == 0:
        hs = "01"
print(hs + ":" + ms)
