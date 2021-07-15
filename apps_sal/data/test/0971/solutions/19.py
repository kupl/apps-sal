n, b, d = list(map(int, input().split(' ')))
a = list(map(int, input().split(' ')))

level = 0
overflows = 0

for ai in a:
    if ai > b: continue
    level += ai
    if level > d:
        overflows += 1
        level = 0
        
print(overflows)

