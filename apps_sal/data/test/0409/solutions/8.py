def ham(a, b):
    if a[1] == b[0] or b[1] == a[0]:
        return 0
    return 1


a = input()
ab = []
ba = []
for i in range(len(a) - 1):
    if a[i:i + 2] == "AB":
        ab.append([i, i + 1])
    if a[i:i + 2] == "BA":
        ba.append([i, i + 1])
s = 0
for i in range(len(ab)):
    for l in range(len(ba)):
        if ham(ab[i], ba[l]):
            print("YES")
            s = 1
            break
    if s == 1:
        break
if s == 0:
    print("NO")
