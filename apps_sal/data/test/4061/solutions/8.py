s = input()
t = input()

pos = [[-1, -1] for i in range(len(t))]

ptr = 0
for i,c in enumerate(t):
    while s[ptr] != c:
        ptr += 1
    pos[i][0] = ptr
    ptr += 1

ptr = len(s) - 1
for i in range(len(t)-1, -1, -1):
    c = t[i]
    while s[ptr] != c:
        ptr -= 1
    pos[i][1] = ptr
    ptr -= 1

best = max(pos[0][1], len(s)-pos[-1][0]-1)
for i in range(1, len(pos)):
    best = max(best, pos[i][1] - pos[i-1][0] - 1)

print(best)

