s = input()

abfound = bafound = -1
for i in range(len(s) - 1):
    if abfound == -1 and s[i] == 'A' and s[i + 1] == 'B':
        abfound = i
    elif bafound == -1 and s[i] == 'B' and s[i + 1] == 'A':
        bafound = i
    if abfound != -1 and bafound != -1:
        break

if abfound == -1 or bafound == -1:
    print("NO")
    return

if abfound == bafound + 1 or bafound == abfound + 1:
    for i in range(max(bafound + 2, abfound + 2), len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            newabfound = True
            print("YES")
            return
        elif s[i] == 'B' and s[i + 1] == 'A':
            newbafound = True
            print("YES")
            return
else:
    print("YES")
    return

print("NO")

