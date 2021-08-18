used = []
a = input().replace("{", "").replace("}", "").replace(" ", "").split(",")
if a == [""]:
    print("0")
else:
    for b in a:
        if b not in used:
            used.append(b)
    print(len(used))
