(x, y, z) = list(map(int, input().split()))
max_c = (x + y) // z
e_1 = x % z
e_2 = y % z
ex = 0
if e_1 + e_2 >= z:
    ex = min(z - e_1, z - e_2)
print(max_c, ex)
