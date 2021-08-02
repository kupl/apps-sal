# You lost the game.
t, s, x = list(map(int, input().split()))
e = x - t
v = e % s
if (x >= t + s and (v == 0 or v == 1)) or (x == t):
    print("YES")
else:
    print("NO")
