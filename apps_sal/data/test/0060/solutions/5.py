pos = input()
row = int(pos[:-1]) - 1
place = pos[-1]

res = 0
res += (row // 4) * 16

if row % 2 != 0:
    res += 7

res += 'fedabc'.index(place) + 1

print(res)

