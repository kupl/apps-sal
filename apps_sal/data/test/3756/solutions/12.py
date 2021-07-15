n, t = map(int, input().split())

s = input()
ind = s.find(".")

for i in range(ind+1, n):
    if s[i] > "4":
        break
else:
    print(s)
    quit()

while t:
    t -= 1
    i -= 1
    if s[i] < "4":
        break

if i > ind:
    print(s[:i], chr(ord(s[i])+1), sep = "")
else:
    t = list(s[:i])
    for i in range(len(t)-1, -1, -1):
        if t[i] == "9":
            t[i] = "0"
        else:
            t[i] = chr(ord(t[i])+1)
            break
    else:
        t.insert(0, "1")

    print("".join(t))

