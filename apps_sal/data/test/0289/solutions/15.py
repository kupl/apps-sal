x = input()
t = x.count("VK")
l = x.replace("VK", " ")
if "KK" in l:
    t += 1
    print(t)
elif "VV" in l:
    t += 1
    print(t)
else:
    print(t)
