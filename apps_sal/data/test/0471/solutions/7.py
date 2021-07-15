# You lost the game.
n,a = list(map(int, input().split()))
L = list(map(int, input().split()))
L.sort()
if n == 1:
    print(0)
elif a >= L[n-1]:
    print(a-L[1])
elif a <= L[0]:
    print(L[n-2]-a)
else:
    gauche = min(abs(a - L[0]),abs(L[n-2] - a)) + L[n-2] - L[0]
    droite = min(abs(a - L[1]),abs(L[n-1] - a)) + L[n-1] - L[1]
    if gauche < droite:
        print(gauche)
    else:
        print(droite)

