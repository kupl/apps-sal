s = input()
slist = list(s)

gs = slist.count("g")
ps = slist.count("p")

if len(slist) % 2 == 0:
    res = (gs - ps) // 2

else:
    res = (gs - 1 - ps) // 2

print(res)
