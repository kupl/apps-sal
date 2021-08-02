n = int(input())
a = "W" + input() + "W"
count = 0
lst = []
for ch in a:
    if ch == "B":
        count += 1
    elif count:
        lst.append(count)
        count = 0
print(len(lst))
print(" ".join(map(str, lst)))
