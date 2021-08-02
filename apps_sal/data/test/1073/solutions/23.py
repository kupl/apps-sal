# You lost the game.
n = int(input())
ch = str(input())
r = 0
a = 0
b = 0
T = [[0, 0]]
for k in range(n):
    if ch[k] == "U":
        a += 1
    elif ch[k] == "D":
        a -= 1
    elif ch[k] == "R":
        b += 1
    else:
        b -= 1
    T += [[a, b]]

for i in range(1, n + 1):
    for j in range(i):
        if T[j] == T[i]:
            r += 1

print(r)
