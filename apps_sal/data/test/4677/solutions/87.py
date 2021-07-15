s = input()
L = []
for x in s:
    if x == "0":
        L.append("0")
    elif x == "1":
        L.append("1")
    else:
        if len(L) >= 1:
            del L[-1]
print("".join(L))
