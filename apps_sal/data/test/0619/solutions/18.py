x, y, z = map(int, input().split())
mod1 = x % z
mod2 = y % z

if (mod1 + mod2) >= z:
    print(x // z + y // z + 1, z - max(mod1, mod2))
else:
    print(x // z + y // z, 0)
