s = input()
al = "abcdefghijklmnopqrstuvwxyz"
f = True
for e in al:
    if s.count(e) % 2 != 0:
        f = False
        break
print("Yes" if f else "No")
