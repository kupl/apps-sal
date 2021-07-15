x = y = 0

m = []

for i in range(5):
    m.append([s for s in input().split(" ")])
    
for n, i in enumerate(m):
    if "1" in i:
        y = n
        x = i.index("1")

print(abs(2 - x) + abs(2 - y))
