n = int(input())
bad = True
for i in range(n):
    line = input().split()
    name, start, finish = line[0], int(line[1]), int(line[2])
    if start >= 2400 and finish > start:
        bad = False
if not bad:
    print("YES")
else:
    print("NO")

