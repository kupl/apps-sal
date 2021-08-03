n = int(input())
t = input()

baseS = "110"
lenS = 10**10
if t == "0":
    out = lenS
elif t == "1":
    out = lenS * 2
# elif t == "11":
#    out = lenS*2
else:
    out = 0
    for chOffset in range(3):
        iter = (chOffset + n + 2) // 3
        num1 = lenS - iter + 1

        isMatched = True
        for j in range(n):
            if t[j] != baseS[(j + chOffset) % 3]:
                isMatched = False

        if isMatched:
            out += num1

print(out)
