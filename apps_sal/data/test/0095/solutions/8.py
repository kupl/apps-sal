n = int(input())

prev = 0
f = 0

for v in map(int, input().split()):
    if v > prev:
        if f > 0:
            print("NO")
            return
    elif v == prev:
        if f == 2:
            print("NO")
            return
        f = 1
    else:
        f = 2
    prev = v

print("YES")
