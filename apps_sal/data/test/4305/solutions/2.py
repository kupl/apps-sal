h, a = map(int, input().split())
hitpoint = h
count = 0
while hitpoint > 0:
    hitpoint -= a
    count += 1
print(count)
