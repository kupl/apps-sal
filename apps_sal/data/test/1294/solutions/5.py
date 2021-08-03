l = []
for i in range(int(input())):
    x = input().upper()
    ly = ""
    for i in range(65, 91):
        ch = chr(i)
        if x.replace(ch + ch, "").find(ch) != -1:
            ly += ch.lower()
    l.append(ly)

print("\n".join(l))
