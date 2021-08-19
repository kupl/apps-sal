n = int(input())
seq = list(map(int, input().split(' ')))
tot = 0
for x in seq:
    if x < 0:
        tot += -x
    else:
        tot += x
print(tot)
