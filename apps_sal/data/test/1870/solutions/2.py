# You lost the game.

n, c = list(map(int, input().split()))
L = list(map(int, input().split()))
r = 1
for i in range(1, n):
    if L[i] - L[i - 1] > c:
        r = 1
    else:
        r += 1
print(r)
