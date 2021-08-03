n, m = list(map(int, input().split()))
buttons = list(map(int, input().split()))
lamps = [0] * n
for i in buttons:
    l = i - 1
    while (l < n) and not lamps[l]:
        lamps[l] = i
        l += 1
print(" ".join(list(map(str, lamps))))
