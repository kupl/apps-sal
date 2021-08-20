import itertools as it
N = int(input())
MARCH = [0, 0, 0, 0, 0]
for i in range(0, N):
    S = str(input())
    if S[0] == 'M':
        MARCH[0] += 1
    if S[0] == 'A':
        MARCH[1] += 1
    if S[0] == 'R':
        MARCH[2] += 1
    if S[0] == 'C':
        MARCH[3] += 1
    if S[0] == 'H':
        MARCH[4] += 1
mokou = list(it.product([0, 1], repeat=5))
count = 0
for i in range(0, len(mokou)):
    if sum(mokou[i]) == 3:
        zen = 1
        for j in range(0, 5):
            if mokou[i][j] == 1:
                zen = zen * MARCH[j]
        count += zen
print(count)
