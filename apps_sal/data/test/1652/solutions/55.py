S = input()

L = ["eraser", "erase", "dreamer", "dream"]

while len(S) > 0:
    for i in range(len(L)):
        if L[i] in S:
            S = S.replace(L[i], "")
    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")
