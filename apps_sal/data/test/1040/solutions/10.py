N = int(input())
r = []
for i in list(input()):
    r.append(i)
    while 1:
        if 3 <= len(r) and r[len(r) - 3:] == ["f", "o", "x"]:
            for j in range(3):
                r.pop()
        else:
            break
print(len(r))
