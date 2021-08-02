n = int(input())
s = input()
tCap = []
shortest = n
l = 0
for r in range(n):
    if s[r] not in tCap:
        tCap += s[r]
        shortest = r - l + 1
    else:
        while s[l] in s[l + 1:r + 1]:
            l += 1
        if r - l + 1 < shortest:
            shortest = r - l + 1
print(shortest)
