import math
n, h, k = map(int, input().split())

seconds = 0
filledSpace = 0
potatoes = list(map(int, input().split()))

for p in potatoes:
    if p + filledSpace <= h:
        filledSpace += p
    else:
        s = math.ceil((p - (h - filledSpace)) / k)
        if s * k > filledSpace:
            filledSpace = 0
        else:
            filledSpace -= s * k
        seconds += s
        filledSpace += p

s = math.ceil(filledSpace / k)
seconds += s

print(str(seconds))
