line1 = input().split()
n = int(line1[0])
m = int(line1[1])
black = True
for i in range(n):
    line = input().split()
    for c in line:
        if c == "W" or c == "B" or c == "G":
            pass
        else:
            black = False
if black:
    print("
else:
    print("
