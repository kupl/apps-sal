n = int(input())
s = input()

place = 0
res = 0
prev_place = 0

for c in s:
    if c == "U":
        place += 1
    else:
        place -= 1
    if place != 0:
        if place * prev_place < 0:
            res += 1
        prev_place = place

print(res)
