a, b = list(map(int, input().split(' ')))
bad = a
for i in range(133742):
    bad = bad*2
    if bad % b == 0:
        print("Yes")
        quit()
    else:
        bad %= b
print("No")

