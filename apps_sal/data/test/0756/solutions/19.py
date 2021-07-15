n = int(input())
last = 0
for t in (int(x) for x in input().split()):
    if t-last > 15:
        break
    last = t
print(min(last+15, 90))

