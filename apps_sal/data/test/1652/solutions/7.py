S = input()
S = S[::-1]
key = [
    "dream"[::-1],
    "erase"[::-1],
    "dreamer"[::-1],
    "eraser"[::-1]
]
f = False
while(S != ""):
    f = False
    for i in range(4):
        tmp = S[0:len(key[i])]
        if (tmp == key[i]):
            S = S[len(key[i]):]
            f = True
            break
    if not(f):
        break

if (f):
    print("YES")
else:
    print("NO")
