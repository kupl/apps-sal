N = int(input())
out = 0
for items in range(N):
    if (items + 1) % 3 != 0 and (items + 1) % 5 != 0:
        out += (items + 1)
print(out)
