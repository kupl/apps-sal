a = int(input())
tot = 0
for x in range(1, a):
    tot += (x * (a - x))
tot += a
print(tot)
