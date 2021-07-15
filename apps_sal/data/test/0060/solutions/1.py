# You lost the game.
s = str(input())
l = s[len(s)-1]
r = int(s[:len(s)-1]) - 1

D = {}
D["f"] = 1
D["e"] = 2
D["d"] = 3
D["a"] = 4
D["b"] = 5
D["c"] = 6

q = r // 4
b = r % 4

if b % 2 == 0:
    print(D[l]+16*q)
else:
    print(D[l]+16*q+7)

