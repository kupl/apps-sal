# You lost the game.

n = int(input())

T = {}


T[1] = 2
T[2] = 3
T[3] = 5
T[4] = 8

t = 1
r = 0
while r < 4 and t <= n:
    r += 1
    t = T[r]

while t <= n:
    r += 1
    t += T[r - 2]
    T[r] = t

print(r - 1)
