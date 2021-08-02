k = int(input())
s = 0
for x in range(1, k + 1):
    for y in range(1, k + 1):
        if y % 2 == 1 and x % 2 == 0:
            s = s + 1
print(s)
