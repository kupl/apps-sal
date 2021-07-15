n = int(input())
magnit = input()
island = 1
for i in range(n - 1):
    if magnit != input():
        island += 1
        magnit = magnit[::-1]
print(island)
