sa = input()
if sa == "{}":
    print(0)
else:
    sa2 = []
    for x in range(1, len(sa), 3):
        sa2.append(sa[x])
    sa3 = list(set(sa2))
    print(len(sa3))
