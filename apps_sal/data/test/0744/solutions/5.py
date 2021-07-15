n = int(input())
sl = input()

sf = 0
fs = 0

last = "-1"
for x in sl:
    if last == "-1" or last == x:
        last = x
        continue
    elif last == "S" and x == "F":
        sf += 1
    else:
        fs += 1
    last = x

if (sf > fs):
    print("YES")
else:
    print("NO")
