import sys
have = input()
need = input()
pl = 0
alph = "abcdefghijklmnopqrstuvwxyz"
for l in alph:
    if l in need:
        if l not in have:
            print(-1)
            return
        pl += min(have.count(l), need.count(l))
print(pl)
